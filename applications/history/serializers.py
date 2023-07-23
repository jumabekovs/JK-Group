from rest_framework import serializers
from .models import History, ExtraFields


class HistoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFields
        fields = "__all__"

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.picture.url
            requests = self.context.get("request")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url


class HistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['extra'] = HistoryImageSerializer(instance.extrafields.all(), many=True).data
        representation['company'] = str(instance.company)
        return representation


class HistoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['extra'] = HistoryImageSerializer(instance.extrafields.all(), many=True).data
        representation['company'] = str(instance.company)
        return representation
