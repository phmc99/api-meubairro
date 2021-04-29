from rest_framework import viewsets
from app_comercios.api import serializers
from app_comercios import models 

from rest_framework import filters

class ComerciosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ComerciosSerializer
    queryset = models.Comercios.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'categoria', 'bairro']