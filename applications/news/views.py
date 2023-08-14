from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, PostPage
from .serializers import PostListSerializer, PostDetailSerializer, PostPageSerializer
from django_filters import rest_framework as filters

from .filters import PostFilter


class PostPageView(ListAPIView):
    queryset = PostPage.objects.all()
    serializer_class = PostPageSerializer
    pagination_class = None


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = PostFilter
    pagination_class = None
    search_fields = ['title', 'title_ru', 'title_ky', 'title_en']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'status': 'success',
            'data': response.data,
            'info': PostPageSerializer(PostPage.objects.first()).data
        }
        return response


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
