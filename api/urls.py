"""Stores urls"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r"message", views.MessageViewSet, basename="message")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path("token/", views.ObtainTokenView.as_view(), name="obtain_token"),
]
