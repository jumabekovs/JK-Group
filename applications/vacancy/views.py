from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Vacancy
from .serializers import VacancyListSerializer, VacancyDetailSerializer
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from .filters import VacancyFilter


class VacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VacancyFilter
    pagination_class = PageNumberPagination


class VacancyDetailView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer
