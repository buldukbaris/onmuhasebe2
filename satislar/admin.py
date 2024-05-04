from django.contrib import admin
from .models import Satis
from decimal import Decimal
from django.contrib import messages


class SatisAdmin(admin.ModelAdmin):
    list_display = ["stok_adi", "miktar", "birimi", "kdv_orani", "kdvhsatis_fiyati", "kdvdsatis_fiyati", "cari_adi"]
    search_fields = ["stok_adi"]  # Doğru alan adını buraya ekleyin
    """list_filter = ["created_date"]"""

    class Meta:
        model = Satis

    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = "Seçili Kaydı Sil"

@admin.register(Satis)
class SatisAdmin(SatisAdmin):
    pass
