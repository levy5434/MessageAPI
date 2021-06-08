from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Message model serializer."""

    class Meta:
        """Serializer based on Message model."""

        model = Message
        fields = "__all__"
        extra_kwargs = {
            "views_counter": {"read_only": True},
        }

    def create(self, validated_data: dict) -> object or None:
        """
        Creates Message object.

        Args:
            validated_data(dict): Data to serialize.

        Returns:
            object: Message object or None.
        """
        if not self.is_valid():
            return None
        new_message = Message(text=self.validated_data["text"])
        new_message.save()
        return new_message


class EmailSerializer(serializers.Serializer):
    """Email serializer."""

    email = serializers.EmailField()
