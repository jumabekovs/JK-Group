from django_filters import rest_framework as filters
from .models import Main


# class MultiModelSearchFilter(filters.FilterSet):
#     search = filters.CharFilter(method='search_filter')
#
#     class Meta:
#         model = Main
#         fields = ['search']
#
#     def search_filter(self, queryset, name, value):
#         return queryset.filter(name__icontains=value) | ModelB.objects.filter(name__icontains=value)