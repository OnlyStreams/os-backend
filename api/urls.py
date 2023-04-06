from django.urls import path

from .views import ApiIndexView

urlpatterns = [
    path("", ApiIndexView.as_view()),
]
