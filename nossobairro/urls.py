from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.views.generic import TemplateView


from rest_framework import routers

from app_comercios.api import viewsets as comerciosviewsets

route = routers.SimpleRouter()
route.register(r'comercios', comerciosviewsets.ComerciosViewSet, basename='Comercios')

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
