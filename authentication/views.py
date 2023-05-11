from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, permissions

from authentication.serializer import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
