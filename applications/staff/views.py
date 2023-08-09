from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Team, TeamPage
from .serializers import TeamSerializer, TeamPageSerializer
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'status': 'success',
            'data': response.data,
            'info': TeamPageSerializer(TeamPage.objects.first()).data
        }
        return response


class TeamDetailView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
