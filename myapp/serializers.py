from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, UserRole

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined']

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_name = validated_data.pop('role', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        if role_name:
            role, created = Role.objects.get_or_create(name=role_name)
            UserRole.objects.create(user=user, role=role)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)