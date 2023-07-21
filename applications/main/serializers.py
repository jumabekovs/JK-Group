from rest_framework import serializers
from .models import Main
from ..line.models import Line
from ..line.serializers import LineListSerializer
from ..project.models import Project
from ..staff.models import Team


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__"

    def get_video_url(self, obj):
        if obj.main_video:
            url = obj.main_video.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['main_video'] = self.get_video_url(instance)
        representation['lines'] = LineListSerializer(Line.objects.all(), many=True).data
        representation['statistics'] = {'Projects': Project.objects.all().count(), 'Lines of Bussiness':
            Line.objects.all().count(), 'Team members': Team.objects.all().count()}
        return representation
