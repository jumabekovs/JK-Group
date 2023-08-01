from rest_framework import serializers
from .models import Line, ExtraFields
from ..project.serializers import ProjectListSerializer
from ..staff.serializers import TeamSerializer


class LineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        exclude = ('sub_title', 'sub_title_ru', 'sub_title_ky', 'sub_title_en')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['company'] = str(instance.company)
        representation['extra_fields'] = LineImageSerializer(instance.extrafields.all(), many=True).data + \
                                         [instance.sub_title_ru, instance.sub_title_ky,instance.sub_title_en]
        representation['team'] = TeamSerializer(instance.lines.all(), many=True).data
        return representation


class LineImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFields
        fields = "__all__"

    def _get_image_url(self, obj):
        if obj.picture:
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
        representation['extra_fields'] = LineImageSerializer(instance.extrafields.all(), many=True).data
        representation['company'] = str(instance.company)
        representation['projects'] = ProjectListSerializer(instance.projects.all(), many=True).data
        return representation
