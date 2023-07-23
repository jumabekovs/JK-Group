from rest_framework import serializers
from .models import Career, CareerImages


class CareerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"

    def get_video_url(self, obj):
        if obj.main_video:
            url = obj.main_video.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = CareerImageSerializer(instance.images.all(), many=True).data
        representation['main_video'] = self.get_video_url(instance)
        return representation


class CareerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerImages
        fields = ('picture',)

    def get_video_url(self, obj):
        if obj.main_video:
            url = obj.main_video.url
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

    def get_video_url(self, obj):
        if obj.main_video:
            url = obj.main_video.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = CareerImageSerializer(instance.images.all(), many=True).data
        representation['main_video'] = self.get_video_url(instance)
        return representation
