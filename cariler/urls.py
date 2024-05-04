# cari/urls.py

from django.urls import path
from .views import cari_ekle

urlpatterns = [
    path('ekle/', cari_ekle, name='cari_ekle'),
    # Diğer URL desenleri buraya eklenebilir
]
