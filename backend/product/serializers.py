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
            "profile",
            "get_feed_poster",
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

class FeedDetailSerializer(serializers.ModelSerializer):
    pass
# serializer에 feed , comment model 병합 response할 field 정하기