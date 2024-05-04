from django.contrib import admin
from .models import Cari

# Register your models here.

@admin.register(Cari)


class CariAdmin(admin.ModelAdmin):
    list_display = ["cari_adi","vergi_dairesi","vergi_no","telefon","email","cariDurum","Borc","Alacak","Bakiye"]
    search_fields = ["Cari"]
    """list_filter = ["created_date"]"""

    class Meta:
        model = Cari
