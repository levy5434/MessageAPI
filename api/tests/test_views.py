from django.contrib.auth.models import User
from rest_framework.test import APIClient, APIRequestFactory
from django.urls import reverse
import pytest
from api.views import MessageViewSet, ObtainTokenView
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestObtainTokenView:
    """Tests ObtainTokenView."""

    factory = APIRequestFactory()

    def test_valid_data(self):
        """Tests valid data view."""
        url = reverse("api:obtain_token")
        request = self.factory.post(url, {"email": "test@test.com"})
        response = ObtainTokenView.as_view()(request)
        assert response.data == {
            "Success": "Token has been sent to your email. Use it to authenticate your API calls."
        }
        assert response.status_code == 200

    def test_invalid_email(self):
        """Tests invalid email."""
        url = reverse("api:obtain_token")
        request = self.factory.post(url, {"email": "test"})
        response = ObtainTokenView.as_view()(request)
        assert response.data == {"email": ["Enter a valid email address."]}
        assert response.status_code == 400

    def test_no_data(self):
        """Tests invalid email."""
        url = reverse("api:obtain_token")
        request = self.factory.post(url, data=None)
        response = ObtainTokenView.as_view()(request)
        assert response.data == {"email": ["This field is required."]}
        assert response.status_code == 400


@pytest.mark.django_db
class TestMessageViewSet:
    """Tests MessageViewSet."""

    client = APIClient()
    factory = APIRequestFactory()

    @pytest.fixture
    def dummy_user(self):
        """Creates dummy user for authenticating API calls."""
        obj = User.objects.get_or_create(
            username="dummy_user", password="dummy_password"
        )[0]
        return obj

    def test_get_message(self):
        """Tests retrieving single message with no authentication."""
        message = mixer.blend("api.Message", text="Some test text.")
        url = reverse("api:message-detail", kwargs={"pk": 1})
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == {
            "id": 1,
            "text": "Some test text.",
            "views_counter": 1,
        }

    def test_incrementing_message_view_counter(self):
        """Tests incrementing view counter."""
        message = mixer.blend("api.Message", text="Some test text.")
        url = reverse("api:message-detail", kwargs={"pk": 1})
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == {
            "id": 1,
            "text": "Some test text.",
            "views_counter": 1,
        }
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data == {
            "id": 1,
            "text": "Some test text.",
            "views_counter": 2,
        }

    def test_authenticated_create_message(self, dummy_user):
        """Tests creating a message when authenticated."""
        self.client.force_authenticate(user=dummy_user)
        url = reverse("api:message-list")
        response = self.client.post(url, {"text": "Some test text."})
        self.client.force_authenticate(user=None)
        assert response.status_code == 201
        assert response.data == {
            "id": 1,
            "text": "Some test text.",
            "views_counter": 0,
        }

    def test_unauthenticated_create_message(self):
        """Tests creating a message without authentication."""
        url = reverse("api:message-list")
        response = self.client.post(url, {"text": "Some test text."})
        assert response.status_code == 401
        assert (
            response.data["detail"]
            == "Authentication credentials were not provided."
        )

    def test_authenticated_update_message(self, dummy_user):
        """Tests updating a message when authenticated."""
        self.client.force_authenticate(user=dummy_user)
        message = mixer.blend("api.Message", text="Some test text.")
        url = reverse("api:message-detail", kwargs={"pk": 1})
        response = self.client.put(url, {"text": "Updated text."})
        self.client.force_authenticate(user=None)
        assert response.status_code == 200
        assert response.data == {
            "id": 1,
            "text": "Updated text.",
            "views_counter": 0,
        }

    def test_unauthenticated_update_message(self):
        """Tests updating a message without authentication."""
        message = mixer.blend("api.Message", text="Some test text.")
        url = reverse("api:message-detail", kwargs={"pk": 1})
        response = self.client.put(url, {"text": "Updated text."})
        assert response.status_code == 401
        assert (
            response.data["detail"]
            == "Authentication credentials were not provided."
        )

    def test_authenticated_delete_message(self, dummy_user):
        """Tests deleting a message when authenticated."""
        self.client.force_authenticate(user=dummy_user)
        message = mixer.blend("api.Message", text="Some test text.")
        url = reverse("api:message-detail", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.client.force_authenticate(user=None)
        assert response.status_code == 204
        assert response.data == {
            "Response": "Message has been successfully deleted."
        }

    def test_unauthenticated_delete_message(self):
        """Tests updating a message without authentication."""
        message = mixer.blend("api.Message", text="Some test text.")
        url = reverse("api:message-detail", kwargs={"pk": 1})
        response = self.client.delete(url)
        assert response.status_code == 401
        assert (
            response.data["detail"]
            == "Authentication credentials were not provided."
        )
