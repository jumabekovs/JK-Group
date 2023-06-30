from django.urls import path
from .views import CreateMailView

urlpatterns = [
    path("", CreateMailView.as_view()),
]
