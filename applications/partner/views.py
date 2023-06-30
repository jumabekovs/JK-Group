from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Partner, PartnerPage
from .serializers import PartnerPageSerializer, PartnerSerializer
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from .filters import PartnerFilter


class PartnerListView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PartnerFilter
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'status': 'success',
            'data': response.data,
            'info': PartnerPageSerializer(PartnerPage.objects.first()).data
        }
        return response


class PartnerDetailView(RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
