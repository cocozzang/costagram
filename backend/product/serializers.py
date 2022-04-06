from rest_framework import serializers

from .models import Feed

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

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