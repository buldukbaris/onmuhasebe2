from django.contrib import admin
from .models import SatinAlma
from decimal import Decimal
from django.contrib import messages


class SatinAlmaAdmin(admin.ModelAdmin):
    list_display = ["stok_adi", "miktar", "birimi", "kdv_orani", "kdvhalis_fiyati", "kdvdalis_fiyati", "cari_adi"]
    search_fields = ["stok_adi"]  # Doğru alan adını buraya ekleyin
    """list_filter = ["created_date"]"""

    class Meta:
        model = SatinAlma

    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = "Seçili Kaydı Sil"

@admin.register(SatinAlma)
class SatinAlmaAdmin(SatinAlmaAdmin):
    pass
