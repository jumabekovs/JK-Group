from rest_framework import serializers
from .models import Project, ExtraFields


class ProjectImageSerializer(serializers.ModelSerializer):
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


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['extra_fields'] = ProjectImageSerializer(instance.extrafields.all(), many=True).data
        representation['lines'] = str(instance.line)
        representation['REFERS'] = str("PROJECTS")
        return representation


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['extra_fields'] = Project(instance.extrafields.all(), many=True).data
        representation['lines'] = str(instance.line)
        return representation

