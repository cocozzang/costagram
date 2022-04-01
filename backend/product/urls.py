from django.urls import path, include
from .views import  FeedList, FeedDetail

urlpatterns = [
    path('', FeedList.as_view()),
    path('feed-detail/<int:feed_id>/', FeedDetail.as_view()),
]