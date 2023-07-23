from rest_framework import serializers
from .models import Team, TeamPage


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['line'] = str(instance.line)
        return representation


class TeamPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPage
        fields = "__all__"
