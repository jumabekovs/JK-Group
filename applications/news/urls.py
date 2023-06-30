from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("all/", PostListView.as_view()),
    path("<int:pk>/", PostDetailView.as_view()),
]
