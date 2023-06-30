from django.urls import path
from .views import HistoryDetailView, HistoryListView

urlpatterns = [
    path("all/", HistoryListView.as_view()),
    path("<int:pk>/", HistoryDetailView.as_view()),
]
