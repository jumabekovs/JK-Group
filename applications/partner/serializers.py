from rest_framework import serializers
from .models import Partner, PartnerPage


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class PartnerPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPage
        fields = "__all__"
