from rest_framework import serializers

from applications.twits.models import *

class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    @staticmethod
    def get_full_name(obj):
        return obj.first_name + " " + obj.last_name

    class Meta:
        model = Customer
        exclude = ()


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=False)

    class Meta:
        model = Order
        exclude = ()


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        exclude = ()

