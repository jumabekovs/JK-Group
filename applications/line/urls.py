from django.urls import path
from .views import LineDetailView, LineListView

urlpatterns = [
    path("all/", LineListView.as_view()),
    path("<int:pk>/", LineDetailView.as_view()),
]
