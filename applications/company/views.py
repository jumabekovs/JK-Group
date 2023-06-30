from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Company
from .serializers import CompanyListSerializer, CompanyDetailSerializer


class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


class CompanyDetailView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
