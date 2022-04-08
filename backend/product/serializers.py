from rest_framework import serializers

from .models import Feed, User

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, TokenSerializer


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            "id",
            "date_posted",
            "description",
            "image",
            "get_absolute_url",
            "get_image",
        )

# djoser/serializers.py에서 settings.py의 AUTH_USER_MODEL = 'product.User' model을 참조
# djoser BaseUserRegistrationSerializer를 상속받아 product.User와 맵핑된 field 추가
class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "username",
            "password",
            "email",
            "nickname",
            "first_name",
            "last_name",
            "profile_image",
            "profile_thumbnail",
            "get_absolute_url",
            "get_profile_thumbnail",
        )
