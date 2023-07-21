from django.db.models import Q
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Main
from .serializers import MainSerializer
from ..line.models import Line
from ..line.serializers import LineListSerializer
from ..news.models import Post
from ..news.serializers import PostListSerializer
from ..partner.models import Partner
from ..partner.serializers import PartnerSerializer
from ..project.models import Project
from ..project.serializers import ProjectListSerializer
from ..staff.models import Team


class MainListView(ListAPIView):
    search_fields = ('title',)
    filter_backends = [SearchFilter]
    serializer_classes = {
        Main: MainSerializer,
        Project: ProjectListSerializer,
        Partner: PartnerSerializer,
        Post: PostListSerializer,
        Line: LineListSerializer,
    }

    def get_serializer_class(self):
        query = self.request.GET.get('search')
        if not query:
            return MainSerializer
        for model, serializer_class in self.serializer_classes.items():
            if model.objects.filter(Q(title__icontains=query) | Q(title_ru__icontains=query) |
                                    Q(title_ky__icontains=query) | Q(title_en__icontains=query)).exists():
                return serializer_class

    def get_queryset(self):
        query = self.request.GET.get('search')
        if not query:
            return Main.objects.all()

        model1_results = Main.objects.filter(Q(title_ru__icontains=query) |
                                             Q(title_ky__icontains=query) | Q(title_en__icontains=query))
        model2_results = Project.objects.filter(Q(title_ru__icontains=query) |
                                                Q(title_ky__icontains=query) | Q(title_en__icontains=query))
        model3_results = Partner.objects.filter(Q(title_ru__icontains=query) |
                                                Q(title_ky__icontains=query) | Q(title_en__icontains=query))
        model4_results = Post.objects.filter(Q(title_ru__icontains=query) |
                                             Q(title_ky__icontains=query) | Q(title_en__icontains=query))

        queryset = list(model1_results) + list(model2_results) + list(model3_results) + \
                   list(model4_results)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        if not queryset or not serializer_class:
            return Response([])
        serializer = serializer_class(queryset, many=True)

        return Response(serializer.data)
