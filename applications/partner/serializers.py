from rest_framework import serializers
from .models import Partner, PartnerPage


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['company'] = str(instance.company)
        return representation


class PartnerPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPage
        fields = "__all__"
