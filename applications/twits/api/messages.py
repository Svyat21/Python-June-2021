from rest_framework import viewsets

from applications.twits.models import Message
from applications.twits.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    model = Message
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all()
