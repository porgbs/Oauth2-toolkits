from django.shortcuts import render
from oauth2_provider.models import Application, RefreshToken, AccessToken
from rest_framework.permissions import AllowAny
from rest_framework import generics, mixins
from .serializers import ApplicationModelSerializer, RefreshTokenModelSerializer, AccessTokenModelSerializer
from django.contrib.auth.models import User


class AppCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationModelSerializer
    permission_classes = (AllowAny,)


class RefreshTokenCreate(generics.CreateAPIView):
    queryset = RefreshToken.objects.all()
    serializer_class = RefreshTokenModelSerializer
    permission_classes = (AllowAny,)


class AccessTokenCreate(generics.CreateAPIView):
    queryset = AccessToken.objects.all()
    serializer_class = AccessTokenModelSerializer
    permission_classes = (AllowAny,)


# class AccessTokenUpdate(generics.UpdateAPIView):
#     queryset = AccessToken.objects.all()
#     serializer_class = AccessTokenModelSerializer
#     permission_classes = (AllowAny,)
class AccessTokenUpdate(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        ):
    serializer_class = AccessTokenModelSerializer
    queryset = AccessToken.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)
