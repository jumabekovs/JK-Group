from django_filters import rest_framework as filters
from .models import Partner


class PartnerFilter(filters.FilterSet):
    class Meta:
        model = Partner
        fields = ('company', )
