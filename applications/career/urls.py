from django.urls import path
from .views import CareerListView, CareerDetailView

urlpatterns = [
    path("all/", CareerListView.as_view()),
    path("<int:pk>/", CareerDetailView.as_view()),
]