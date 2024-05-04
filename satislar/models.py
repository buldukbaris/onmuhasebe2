from django.db import models
from decimal import Decimal



# Create your models here.


class Satis(models.Model):
    stok_adi = models.CharField(max_length=255, verbose_name="Stok Adı")
    stok_kodu = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Stok Kodu")
    barkod = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Barkod")
    miktar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miktar")
    birimi = models.CharField(max_length=255, default="adet", verbose_name="Birimi")
    kdv_orani = models.CharField(max_length=20, default="20", verbose_name="Kdv Oranı")
    kdvhsatis_fiyati = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Kdv Hariç Satış Fiyatı")
    kdvdsatis_fiyati = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Kdv Dahil Satış Fiyatı")
    cari_adi = models.CharField(max_length=255, verbose_name="Cari Adı")
    tutari_kdvharic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Tutar (KDV Hariç)")
    tutari_kdvdahil = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Tutar (KDV Dahil)")
    aciklama = models.CharField(max_length=2550, verbose_name="Açıklama", default="Nakit Tahsilat")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = "Satışlar"
        verbose_name_plural = "Satışlar"

    kdv_dahil = models.BooleanField(default=True, verbose_name="KDV Dahil Mi")
    def save(self, *args, **kwargs):
        # Eğer kdvhalis_fiyati değeri girilmişse, kdvdalis_fiyati'yi hesapla
        if self.kdvhsatis_fiyati is not None:
            self.kdvdsatis_fiyati = self.kdv_haric_satis_fiyati_hesapla()

        # Tutarı hesapla ve kaydet
        self.tutari_kdvharic = self.miktar * self.kdvhsatis_fiyati
        self.tutari_kdvdahil = self.miktar * self.kdvdsatis_fiyati

         # KDV dahil veya KDV hariç seçeneğine göre, ilgili değeri yaz
        self.kdv_dahil = self.kdv_dahil

        super(Satis, self).save(*args, **kwargs)




        


    
    def kdv_haric_satis_fiyati_hesapla(self):
        # Eğer kdvhalis_fiyati değeri girilmemişse, hata fırlat
        if self.kdvhsatis_fiyati is None:
            raise ValueError("Kdv Hariç Satış Fiyatı girilmemiş.")

        # KDV'yi hesapla ve kdvhalis_fiyati'na ekle
        kdv_orani = Decimal(str(self.kdv_orani)) / 100
        return self.kdvhsatis_fiyati * (1 + kdv_orani)


    def __str__(self):
        return self.stok_adi