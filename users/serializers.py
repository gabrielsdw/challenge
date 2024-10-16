from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_of_birth', 'password',]
        

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

class UserDetailModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_of_birth']
