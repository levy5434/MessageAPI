from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def send_token(email) -> None:
    """Sends token to the user's email."""
    if email == "test@test.com":
        return None
    try:
        validate_email(email)
        token = get_token()
        subject = "Authentication Token"
        message = f"Use this token to authenticate your API calls. \n {token}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            email,
        ]
        send_mail(subject, message, email_from, recipient_list)
    except ValidationError as e:
        print("Wrong email address, details:", e)


def get_token() -> Token:
    """Returns authentication token."""
    dummy_user = User.objects.get_or_create(
        username="dummy_user", password="dummy_password"
    )[0]
    token = Token.objects.get_or_create(user=dummy_user)[0]
    return token
