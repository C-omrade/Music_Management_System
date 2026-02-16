from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import AuthenticationFailed
from user.models import CustomUser
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise AuthenticationFailed("Invalid Credentials")
        return user
    

class DumyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','is_subscriber']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"