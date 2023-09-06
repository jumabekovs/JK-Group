from rest_framework import serializers
from .models import Team, TeamPage, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("name", )


class TeamSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Team
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['line'] = str(instance.line)
        representation['department'] = str(instance.department)
        return representation


class TeamPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPage
        fields = "__all__"
