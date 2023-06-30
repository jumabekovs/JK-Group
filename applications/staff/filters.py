from django_filters import rest_framework as filters
from .models import Team


class TeamFilter(filters.FilterSet):
    class Meta:
        model = Team
        fields = ('company', )
