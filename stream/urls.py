from django.urls import path

from stream.views import VerifyStreamKey

urlpatterns = [
    path("verify-key/", VerifyStreamKey.as_view()),
]
