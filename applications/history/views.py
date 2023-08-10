from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import History
from .serializers import HistoryDetailSerializer, HistoryListSerializer


class HistoryListView(ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistoryListSerializer
    pagination_class = None


class HistoryDetailView(RetrieveAPIView):
    queryset = History.objects.all()
    serializer_class = HistoryDetailSerializer
