import json
from itertools import chain

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from requests import Response
from rest_framework import serializers
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Main
from .serializers import MainSerializer
from ..line.models import Line
from ..news.models import Post
from ..news.serializers import PostListSerializer
from ..partner.models import Partner
from ..partner.serializers import PartnerSerializer
from ..project.models import Project
from ..project.serializers import ProjectListSerializer
from ..staff.models import Team


class MainListView(ListAPIView):
    queryset = Main.objects.all()
    search_fields = ('title',)
    filter_backends = [SearchFilter]
    serializer_class = MainSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'status': 'success',
            'data': response.data,
            'statistics': {
                'Projects': Project.objects.all().count(),
                'Lines of Bussiness': Line.objects.all().count(),
                'Team members': Team.objects.all().count()
            }
        }
        return response

