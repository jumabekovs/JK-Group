from rest_framework import serializers
from .models import Main
from ..line.models import Line
from ..line.serializers import LineListSerializer


class MainSerializer(serializers.ModelSerializer):
    # video_url = serializers.SerializerMethodField()

    class Meta:
        model = Main
        exclude = ("main_video",)

    # def get_video_url(self, main):
    #     request = self.context.get('request')
    #     video_url = main.main_video.url
    #     return request.build_absolute_uri(video_url)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lines'] = LineListSerializer(Line.objects.all(), many=True).data
        return representation
