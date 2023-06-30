from rest_framework import serializers
from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
