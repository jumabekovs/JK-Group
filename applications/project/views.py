from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from .filters import ProjectFilter
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectFilter
    pagination_class = PageNumberPagination


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

