from django.urls import path
from .views import CompanyListView, CompanyDetailView

urlpatterns = [
    path("all/", CompanyListView.as_view()),
    path("<int:pk>/", CompanyDetailView.as_view()),
]