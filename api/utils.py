from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


def send_token(email) -> None:
    """Sends token to the user's email."""
    try:
        validate_email(email)
        token = get_token()
        text = f"<p>Recruitment task - KL</p> <p>Use this token to authenticate your API calls.</p> <p>{token}</p>"  # noqa
        message = Mail(
            from_email="rmarsh7@int.pl",
            to_emails=email,
            subject="Authentication token",
            html_content=text,
        )
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_CLIENT"))
        sg.send(message)
    except ValidationError as e:
        print("Wrong email address, details:", e)


def get_token() -> Token:
    """Returns authentication token."""
    dummy_user = User.objects.get_or_create(
        username="dummy_user", password="dummy_password"
    )[0]
    token = Token.objects.get_or_create(user=dummy_user)[0]
    return token

