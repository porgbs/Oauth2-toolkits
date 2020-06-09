from rest_framework import serializers
from oauth2_provider.models import Application, RefreshToken, AccessToken


class ApplicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class RefreshTokenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefreshToken
        fields = '__all__'


class AccessTokenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessToken
        fields = '__all__'
