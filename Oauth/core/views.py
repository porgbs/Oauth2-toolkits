from django.shortcuts import render
from oauth2_provider.models import Application
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import ApplicationModelSerializer
from django.contrib.auth.models import User


class AppCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationModelSerializer
    permission_classes = (AllowAny,)


