from rest_framework import viewsets

from applications.twits.models import Post
from applications.twits.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    model = Post
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Post.objects.all()
