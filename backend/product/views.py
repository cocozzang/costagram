from django.http import Http404
from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Feed
from .serializers import FeedSerializer

class FeedList(APIView):
    def get(self, request, format=None):
        feeds = Feed.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedDetail(APIView):
    def get(self, request, feed_id, format=None):
        try:
            feed = Feed.objects.get(pk=feed_id)
            serializer = FeedSerializer(feed)
            return Response(serializer.data)
        except Feed.DoesNotExist:
            raise Http404

    def put(self, request, feed_id, format=None):
        feed = Feed.objects.get(pk=feed_id)
        context = request.data
        serializer = FeedSerializer(feed, data=context, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, feed_id, format=None):
        feed = Feed.objects.get(pk=feed_id)
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)