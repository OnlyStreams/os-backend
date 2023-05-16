from django.urls import include, path
from rest_framework import routers

from stream.views import (
    GetStreamKeyView,
    MeView,
    StreamModifyView,
    StreamViewSet,
    VerifyStreamKeyView,
)

router = routers.SimpleRouter()
router.register(r"", StreamViewSet)

urlpatterns = [
    path("me/", MeView.as_view()),
    path("verify-key/", VerifyStreamKeyView.as_view()),
    path("key/", GetStreamKeyView.as_view()),
    path("modify/", StreamModifyView.as_view()),
    path("", include(router.urls)),
]
