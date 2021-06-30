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


class PersonSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField(method_name='get_following')
    followers = serializers.SerializerMethodField(method_name='get_followers')

    @staticmethod
    def get_following(obj):
        return [i.pk for i in obj.following.all()]

    @staticmethod
    def get_followers(obj):
        return [i.pk for i in obj.followers.all()]

    class Meta:
        model = Person
        exclude = ()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'date_creation', 'author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()
