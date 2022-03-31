from rest_framework import serializers

from .models import Feed

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