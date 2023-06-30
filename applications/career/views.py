from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Career
from .serializers import CareerListSerializer, CareerDetailSerializer


class CareerListView(ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerListSerializer


class CareerDetailView(RetrieveAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerDetailSerializer

