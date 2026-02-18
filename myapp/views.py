from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .permission import HasRole

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=400)
        
class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated, HasRole]
    required_role = 'Teacher'  # Example role required to access this view

    def get(self, request, *args, **kwargs):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({
            'message': 'Welcome to the dashboard!',
            'user': user_serializer.data
        }, 200)