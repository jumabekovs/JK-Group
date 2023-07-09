from rest_framework import serializers
from .models import Vacancy, CV


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"
