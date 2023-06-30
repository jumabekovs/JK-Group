from rest_framework import serializers
from .models import Career, CareerImages


class CareerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"


class CareerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerImages
        fields = ('picture',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.picture.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url


class CareerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = CareerImageSerializer(instance.images.all(), many=True).data
        return representation
