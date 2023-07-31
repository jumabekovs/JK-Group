import io

from PyPDF2 import PdfReader
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from source import settings
from .models import Vacancy, CV
from .serializers import VacancyListSerializer, VacancyDetailSerializer, CVSerializer
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


class CVPostView(CreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
