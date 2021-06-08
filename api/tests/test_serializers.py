import pytest
from api.serializers import EmailSerializer, MessageSerializer


class TestEmailSerializers:
    """Tests EmailSerializer."""

    email_serializer = EmailSerializer

    def test_valid_serializer(self):
        """Tests initial views counter."""
        serializer = self.email_serializer(data={"email": "test@test.com"})
        assert serializer.is_valid()
        assert serializer.validated_data == {"email": "test@test.com"}
        assert serializer.errors == {}

    def test_invalid_email(self):
        """Tests invalid email address format"""
        serializer = self.email_serializer(data={"email": "test"})
        assert not serializer.is_valid()
        assert serializer.data == {"email": "test"}
        assert serializer.errors == {"email": ["Enter a valid email address."]}

    def test_empty_email_address(self):
        """Tests empty email address serializer."""
        serializer = self.email_serializer(data={"email": ""})
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.data == {"email": ""}
        assert serializer.errors == {"email": ["This field may not be blank."]}

    def test_validate_none_data(self):
        """Tests serializer when no data is sent."""
        data = None
        serializer = self.email_serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors == {"non_field_errors": ["No data provided"]}


class TestMessageSerializer:
    """Tests MessageSerializer"""

    message_serializer = MessageSerializer

    @pytest.mark.django_db
    def test_valid_serializer(self):
        """Tests valid serializer."""
        serializer = self.message_serializer(data={"text": "Some test text"})
        assert serializer.is_valid()
        assert serializer.validated_data == {"text": "Some test text"}
        assert serializer.data == {"text": "Some test text"}
        assert serializer.errors == {}
        assert (
            type(serializer.create(serializer.validated_data)) != None
        )  # noqa

    def test_empty_text(self):
        """Tests empty text serializer."""
        serializer = self.message_serializer(data={"text": ""})
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.data == {"text": ""}
        assert serializer.errors == {"text": ["This field may not be blank."]}

    def test_too_long_text(self):
        """Tests serializer when sent text is longer than 160 characters."""
        long_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown"  # noqa
        serializer = self.message_serializer(data={"text": long_text})
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.data == {"text": long_text}
        assert serializer.errors == {
            "text": ["Ensure this field has no more than 160 characters."]
        }

    def test_invalid_datatype(self):
        """Tests invalid data type passed to serializer."""
        serializer = self.message_serializer(data=[{"text": "Some test text"}])
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.data == {}
        assert serializer.errors == {
            "non_field_errors": [
                "Invalid data. Expected a dictionary, but got list."
            ]
        }

    def test_validate_none_data(self):
        """Tests serializer when no data is sent."""
        data = None
        serializer = self.message_serializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors == {"non_field_errors": ["No data provided"]}
