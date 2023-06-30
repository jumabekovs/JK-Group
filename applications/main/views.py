from rest_framework.generics import ListAPIView
from .models import Main
from .serializers import MainSerializer
from ..line.models import Line
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
