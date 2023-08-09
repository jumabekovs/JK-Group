from rest_framework import serializers
from .models import Company, CompanyImage
from ..mission.serializers import MissionSerializer
from ..partner.serializers import PartnerSerializer
from ..vacancy.serializers import VacancyListSerializer


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

