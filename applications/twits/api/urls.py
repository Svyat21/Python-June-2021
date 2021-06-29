from django.urls import path
from rest_framework import routers

from applications.twits.api.messages import MessageViewSet

message_router = routers.DefaultRouter()
message_router.register(r'message', MessageViewSet, basename='application.twits')
urlpatterns = message_router.urls
