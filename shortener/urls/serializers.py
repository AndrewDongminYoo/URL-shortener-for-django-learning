from shortener.models import Users, ShortenedUrls
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from shortener.users.utils import url_count_changer


class UserSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = ("id", "url_count", "organization", "email", "full_name")


class UrlListSerializer(ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = ShortenedUrls
        fields = "__all__"
        # fields = ("id", "nick_name", "prefix", "shortened_url", "creator", "click", "created_via", "updated_at")
        # exclude = ("created_at", "target_url", "expired_at", "category")  # fields or exclude


class UrlCreateSerializer(serializers.Serializer):

    nick_name = serializers.CharField(max_length=50)
    target_url = serializers.CharField(max_length=2000)
    category = serializers.IntegerField(required=False)

    def create(self, validated_data, commit=True):
        instance = ShortenedUrls()
        instance.category = validated_data.get("category", None)
        instance.target_url = validated_data.get("target_url").strip()
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
        return instance

    def update(self, instance, validated_data):
        pass
