from rest_framework import serializers
from .models import Main
from ..line.models import Line
from ..line.serializers import LineListSerializer
from ..news.models import Post
from ..news.serializers import PostDetailSerializer
from ..partner.models import Partner
from ..partner.serializers import PartnerSerializer
from ..project.models import Project
from ..project.serializers import ProjectListSerializer


class MainSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Main
        exclude = ("main_video",)

    def get_video_url(self, main):
        request = self.context.get('request')
        video_url = main.main_video.url
        return request.build_absolute_uri(video_url)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lines'] = LineListSerializer(Line.objects.all(), many=True).data
        return representation

    def to_native(self, obj):
        if isinstance(obj, Post):
            serializer = PostDetailSerializer(obj)
        elif isinstance(obj, Project):
            serializer = ProjectListSerializer(obj)
        elif isinstance(obj, Partner):
            serializer = PartnerSerializer(obj)
        else:
            raise Exception("Not found in any instance!")
        return serializer.data


# class GlobalSearchSerializer(serializers.Serializer):
#     def to_native(self, obj):
#         if isinstance(obj, Post):
#             serializer = PostDetailSerializer(obj)
#         elif isinstance(obj, Project):
#             serializer = ProjectListSerializer(obj)
#         elif isinstance(obj, Partner):
#             serializer = PartnerSerializer(obj)
#         else:
#             raise Exception("Not found in any instance!")
#         return serializer.data
