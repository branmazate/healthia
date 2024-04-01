from rest_framework import serializers
from .models import UserQuery, ChatResponse
from django.contrib.auth.models import User


class UserQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuery
        fields = '__all__'
        
class ChatResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatResponse
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
