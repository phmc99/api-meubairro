# Generated by Django 3.1.7 on 2021-05-03 05:03

import app_comercios.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comercios',
            fields=[
                ('id_comercio', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('telefone1', models.CharField(max_length=255)),
                ('telefone2', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('whatsapp', models.CharField(blank=True, max_length=255)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('icone', models.ImageField(blank=True, upload_to=app_comercios.models.upload_imagem)),
                ('imagem1', models.ImageField(blank=True, upload_to=app_comercios.models.upload_imagem)),
                ('imagem2', models.ImageField(blank=True, upload_to=app_comercios.models.upload_imagem)),
                ('imagem3', models.ImageField(blank=True, upload_to=app_comercios.models.upload_imagem)),
                ('imagem4', models.ImageField(blank=True, upload_to=app_comercios.models.upload_imagem)),
            ],
        ),
    ]
