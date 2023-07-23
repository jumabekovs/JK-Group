from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Line
from .serializers import LineDetailSerializer, LineListSerializer


class LineListView(ListAPIView):
    queryset = Line.objects.all()
    serializer_class = LineListSerializer
    pagination_class = None


class LineDetailView(RetrieveAPIView):
    queryset = Line.objects.all()
    serializer_class = LineDetailSerializer
    pagination_class = None

