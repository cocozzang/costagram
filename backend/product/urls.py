from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.FeedList.as_view()),
]