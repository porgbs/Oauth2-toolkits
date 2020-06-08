from rest_framework import serializers
from oauth2_provider.models import Application


class ApplicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

