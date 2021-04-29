from rest_framework import serializers
from app_comercios import models

class ComerciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comercios
        fields = '__all__'