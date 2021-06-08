from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestMessageModel:
    def test_message_views_counter_initial(self):
        """Tests initial views counter."""
        message = mixer.blend("api.Message")
        assert message.views_counter == 0

    def test_message_text(self):
        """Tests initial views counter."""
        message = mixer.blend("api.Message", text="Some test text")
        assert message.text == "Some test text"
