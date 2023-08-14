from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Partner, PartnerPage
from .serializers import PartnerPageSerializer, PartnerSerializer
from django_filters import rest_framework as filters


class PartnerListView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    pagination_class = None
    search_fields = ['title', 'title_ru', 'title_ky', 'title_en']

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
