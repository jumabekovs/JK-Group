from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

from .filters import PostFilter


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = PostFilter
    pagination_class = None
    search_fields = ['title', 'title_ru', 'title_ky', 'title_en']


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
