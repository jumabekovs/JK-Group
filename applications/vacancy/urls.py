from django.urls import path
from .views import VacancyListView, VacancyDetailView, CVPostView

urlpatterns = [
    path("all/", VacancyListView.as_view()),
    path("<int:pk>/", VacancyDetailView.as_view()),
    path("upload/", CVPostView.as_view()),
]
