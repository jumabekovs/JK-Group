from django_filters import rest_framework as filters
from .models import Vacancy


class VacancyFilter(filters.FilterSet):
    class Meta:
        model = Vacancy
        fields = ('company', )
