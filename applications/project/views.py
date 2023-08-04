from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from .filters import ProjectFilter
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer(queryset, many=True)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ProjectFilter
    pagination_class = PageNumberPagination
    search_fields = ['title', 'title_ru', 'title_ky', 'title_en']


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
