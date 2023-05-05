from django.urls import path

from tokens.views import BalanceView, TipView

urlpatterns = [
    path("balance/", BalanceView.as_view()),
    path("tip/", TipView.as_view()),
]
