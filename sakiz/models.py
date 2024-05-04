# sakiz/models.py

from django.db import models
from cariler.models import Cari
from decimal import Decimal
from django.utils import timezone


class SakizMakinesi(models.Model):
    # Sakız makinesi ile ilgili alanları burada tanımlayabilirsiniz
    cari = models.ForeignKey(Cari, on_delete=models.CASCADE)
    ciroToplam = models.DecimalField(max_digits=10, decimal_places=2, blank=False, help_text='Toplam ciroyu kilogram cinsinden giriniz.')
    ciroTL = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text='Toplam ciroya karşılık gelen TL miktarı.')
    ciroBayi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text='Kilogram Cinsinden Bayi Cirosu')
    ciroBayiTL = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text='TL Cinsinden Bayi Cirosu')
    ciroBuldukTL = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text='TL Cinsinden Bulduk Cirosu')
    verilenTL = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Verilen ciroyu TL cinsinden giriniz.')
    acilanSakiz = models.DecimalField(max_digits=10, decimal_places=2, blank=False, help_text='Açılan sakız miktarını giriniz.')
    acilanTop = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Açılan top miktarını giriniz.')
    verilenOyuncak = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Verilen oyuncak miktarını giriniz.')
    makineNo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Makine No", default="")
    aciklama = models.CharField(max_length=255, blank=True, null=True, verbose_name="Açıklama", default="")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return f"SakizMakinesi {self.id}"

    class Meta:
        ordering = ['-created_date']



    def save(self, *args, **kwargs):
        # Burada ciroToplam alanının değeri ve çarpan (122) kullanılarak ciroTL hesaplanıyor
        if self.ciroToplam:
            try:
                ciro_toplam_numeric = Decimal(str(self.ciroToplam).replace(',', '.'))
                self.ciroTL = (ciro_toplam_numeric * Decimal(122))/1000
            except ValueError:
                self.ciroTL = None
                raise ValueError("Lütfen girdiğiniz değerleri kontrol ediniz.")
            
        # ciroToplam değerinin %30'u ciroBayi'ye atanıyor
        if self.ciroToplam:
            self.ciroBayi = (Decimal(self.ciroToplam) * Decimal(30))/100
        else:
            self.ciroBayi = None

        # ciroBayi değerini 122 ile çarptıktan sonra yüzdeye böler ve ciroBayiTL'ye atar
        if self.ciroBayi:
            self.ciroBayiTL = (self.ciroBayi * Decimal(122))/1000
        else:
            self.ciroBayiTL = None

        # ciroTL ile ciroBayiTL arasındaki farkı hesaplar ve ciroBuldukTL'ye atar
        if self.ciroTL is not None and self.ciroBayiTL is not None:
            self.ciroBuldukTL = self.ciroTL - self.ciroBayiTL
        else:
            self.ciroBuldukTL = None

        super().save(*args, **kwargs)