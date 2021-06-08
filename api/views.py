from api.utils import send_token
from .serializers import EmailSerializer, MessageSerializer
from .models import Message
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from django.contrib.auth.models import Permission


class MessageViewSet(viewsets.ModelViewSet):
    """Viewset for Message model."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_permissions(self) -> Permission:
        """
        Returns permission that this view requires.
        HTTP request methods:
            GET - allow unrestricted access.
            POST, PUT, DELETE - deny permission to any unauthenticated user.
        For any other requests method will deny permission to any user,
        unless user.is_staff is True.
        """
        if self.action in "retrieve":
            permission_classes = [AllowAny]
        elif self.action in ["create", "update", "destroy"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs) -> Response:
        """Returns message and increments views counter."""
        instance = self.get_object()
        instance.views_counter = instance.views_counter + 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs) -> Response:
        """Updates message and resets views counter."""
        data = request.data
        instance = self.get_object()
        instance.text = data["text"]
        instance.views_counter = 0
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs) -> Response:
        """Deletes message."""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"Response": "Message has been successfully deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )


class ObtainTokenView(generics.CreateAPIView):
    """View to send authentication token to user's email."""

    def create(self, request) -> Response:
        """
        Checks if correct email was sent with request,
        if so sends authentication token
        to user's email and returns response with status.
        """
        serializer = EmailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        email = serializer.data["email"]
        send_token(email)
        return Response(
            {
                "Success": "Token has been sent to your email. Use it to authenticate your API calls."  # noqa
            },
            status=status.HTTP_200_OK,
        )
