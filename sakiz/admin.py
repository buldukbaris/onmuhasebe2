# sakiz/admin.py

from django.contrib import admin
from .models import SakizMakinesi
from decimal import Decimal
from django.contrib import messages

class Sakiz(admin.ModelAdmin):
    list_display = [ "ciroToplam", "ciroTL", "ciroBayi", "ciroBayiTL", "ciroBuldukTL", "verilenTL", "acilanSakiz", "acilanTop", "verilenOyuncak", "makineNo", "aciklama", "created_date",]
    search_fields = ["cari__cariadi"]  # Doğru alan adını buraya ekleyin
    list_filter = ["created_date"]

    class Meta:
        model = SakizMakinesi

    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = "Seçili Kaydı Sil"

admin.site.register(SakizMakinesi, Sakiz)
