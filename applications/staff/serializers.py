from rest_framework import serializers
from .models import Team, TeamPage


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPage
        fields = "__all__"
