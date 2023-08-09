from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .models import Vacancy, CV
from .serializers import VacancyListSerializer, VacancyDetailSerializer, CVSerializer
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class VacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class VacancyDetailView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer


class CVPostView(CreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
