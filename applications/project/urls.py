from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("all/", ProjectListView.as_view()),
    path("<int:pk>/", ProjectDetailView.as_view()),
]