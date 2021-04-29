from django.db import models
from uuid import uuid4

# Create your models here.

def upload_imagem(instance, filename):
    return f'{instance.id_comercio}-{filename}'

class Comercios(models.Model):
    #Infos
    id_comercio = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    telefone1 = models.CharField(max_length=255)
    telefone2 = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    whatsapp = models.CharField(max_length=255, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    #Imagens
    icone = models.ImageField(upload_to=upload_imagem, blank=True)
    imagem1 = models.ImageField(upload_to=upload_imagem, blank=True)
    imagem2 = models.ImageField(upload_to=upload_imagem, blank=True)
