from rest_framework import viewsets

from applications.twits.models import Post
from applications.twits.serializers import PostSerializer


class MessageViewSet(viewsets.ModelViewSet):
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
