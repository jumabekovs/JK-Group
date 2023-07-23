from rest_framework.serializers import ModelSerializer
from .models import AboutUs


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"
