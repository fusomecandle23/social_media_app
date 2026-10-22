from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
 
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']
         
         
class commentserializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['owner', 'created_at']  
         
         
class likeserializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['id', 'owner_obj', 'created_at']