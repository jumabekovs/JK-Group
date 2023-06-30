from rest_framework import serializers
from .models import Line, ExtraFields
from ..project.serializers import ProjectListSerializer


class LineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['company'] = str(instance.company)
        return representation


class LineImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFields
        fields = "__all__"

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.picture.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url


class LineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = LineImageSerializer(instance.extrafields.all(), many=True).data
        representation['company'] = str(instance.company)
        representation['projects'] = ProjectListSerializer(instance.projects.all(), many=True).data
        return representation
