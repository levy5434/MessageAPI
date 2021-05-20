from django.db import models
from django.core.validators import MinLengthValidator


class Message(models.Model):
    """
    Represents text message and view counter.

    Attributes:
        text (str): Text message with 1 to 160 characters.
        views_counter (int): Stores views counter.
    """

    text = models.CharField(max_length=160, validators=[MinLengthValidator(1)])
    views_counter = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        """Returns string representation of Message object."""
        return f"{self.text}"
