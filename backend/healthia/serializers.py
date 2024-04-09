from rest_framework import serializers
from .models import UserQuery, ChatResponse
from django.contrib.auth.models import User

        
class ChatResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatResponse
        fields = {'response_text','timestamp'}
        
class UserQuerySerializer(serializers.ModelSerializer):
    responses = ChatResponseSerializer(many=True, read_only=True, source='chatresponse_set')
    
    class Meta:
        model = UserQuery
        fields = ['id','query_text','timestamp','responses']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
