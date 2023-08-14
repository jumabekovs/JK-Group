from rest_framework import serializers
from .models import Post, PostPage


class PostPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPage
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = str(instance.category)
        representation['REFERS'] = "NEWS"
        return representation


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
