from shortener.models import Users, ShortenedUrls
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = ("id", "url_count", "organization", "email", "full_name")


class UrlListSerializer(ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = ShortenedUrls
        fields = ("id", "nick_name", "prefix", "shortened_url", "creator", "click", "created_via", "expired_at", "created_at")
