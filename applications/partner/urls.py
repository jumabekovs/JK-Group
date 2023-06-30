from django.urls import path
from .views import PartnerListView, PartnerDetailView

urlpatterns = [
    path("all/", PartnerListView.as_view()),
    path("<int:pk>/", PartnerDetailView.as_view()),
]