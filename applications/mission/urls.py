from django.urls import path
from .views import MissionListView

urlpatterns = [
    path("", MissionListView.as_view()),
]
