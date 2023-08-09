from rest_framework.generics import ListAPIView
from .models import Mission
from .serializers import MissionSerializer


class MissionListView(ListAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
