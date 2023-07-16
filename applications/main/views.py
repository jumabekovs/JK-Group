from itertools import chain

from django.db.models import Q
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .models import Main
from .serializers import MainSerializer
from ..line.models import Line
from ..news.models import Post
from ..partner.models import Partner
from ..project.models import Project
from ..staff.models import Team


class MainListView(ListAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'status': 'success',
            'data': response.data,
            'Projects': Project.objects.all().count(),
            'Lines of Bussiness': Line.objects.all().count(),
            'Team members': Team.objects.all().count()
        }
        return response

#
# class GlobalSearchList(ListAPIView):
#     serializer_class = GlobalSearchSerializer
#     filter_backends = [SearchFilter, ]
#
#     def get_queryset(self):
#         query = self.request.query_params.get('query', None)
#         news = Post.objects.filter(Q(host__icontains=query) | Q(title__icontains=query))
#         projects = Project.objects.filter(Q(name__icontains=query))
#         partners = Partner.objects.filter(Q(title__icontains=query))
#         all_results = list(chain(news, projects, partners))
#         serialize_obj = serializers.serialize('json', all_results)
#         print(serialize_obj)  # Json response is printed in console
#         return JsonResponse(json.loads(serialize_obj), safe=False)  # nothing as output
