from django.urls import include, path
from rest_framework import routers

from stream.views import (
    GetStreamKeyView,
    MeView,
    OnStreamPlayDoneView,
    OnStreamPlayView,
    OnStreamPublishDoneView,
    OnStreamPublishView,
    StreamModifyView,
    StreamViewSet,
)

router = routers.SimpleRouter()
router.register(r"", StreamViewSet)

urlpatterns = [
    path("me/", MeView.as_view()),
    path("on_publish/", OnStreamPublishView.as_view()),
    path("on_publish_done/", OnStreamPublishDoneView.as_view()),
    path("on_play/", OnStreamPlayView.as_view()),
    path("on_play_done/", OnStreamPlayDoneView.as_view()),
    path("key/", GetStreamKeyView.as_view()),
    path("modify/", StreamModifyView.as_view()),
    path("", include(router.urls)),
]
