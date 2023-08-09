from django.urls import path
from .views import CreateMailView, TabView

urlpatterns = [
    path("send-mail/", CreateMailView.as_view()),
    path("", TabView.as_view()),
]
