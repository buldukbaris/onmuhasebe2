from django.db import models
from decimal import Decimal






# Create your models here.


class SatinAlma(models.Model):
    stok_adi = models.CharField(max_length=255, verbose_name="Stok Adı")
    stok_kodu = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Stok Kodu")
    barkod = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Barkod")
    miktar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miktar")
    birimi = models.CharField(max_length=255, default="adet", verbose_name="Birimi")
    kdv_orani = models.CharField(max_length=20, default="20", verbose_name="Kdv Oranı")
    kdvhalis_fiyati = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Kdv Hariç Alış Fiyatı")
    kdvdalis_fiyati = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Kdv Dahil Alış Fiyatı")
    cari_adi = models.CharField(max_length=255, verbose_name="Cari Adı")
    tutari_kdvharic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Tutar (KDV Hariç)")
    tutari_kdvdahil = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="Tutar (KDV Dahil)")
    aciklama = models.CharField(max_length=2550, verbose_name="Açıklama", default="Nakit Ödeme")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = "Satın Alma"
        verbose_name_plural = "Satın Alma"

    kdv_dahil = models.BooleanField(default=True, verbose_name="KDV Dahil Mi")
    def save(self, *args, **kwargs):
        # Eğer kdvhalis_fiyati değeri girilmişse, kdvdalis_fiyati'yi hesapla
        if self.kdvhalis_fiyati is not None:
            self.kdvdalis_fiyati = self.kdv_haric_alis_fiyati_hesapla()
        else:
        # kdvhalis_fiyati değeri girilmemişse, kdvdalis_fiyati üzerinden hesapla
            self.kdvhalis_fiyati = self.kdvdalis_fiyati / (1 + (Decimal(str(self.kdv_orani)) / 100))

        # Tutarı hesapla ve kaydet
        self.tutari_kdvharic = self.miktar * self.kdvhalis_fiyati
        self.tutari_kdvdahil = self.miktar * self.kdvdalis_fiyati

         # KDV dahil veya KDV hariç seçeneğine göre, ilgili değeri yaz
        self.kdv_dahil = self.kdv_dahil

        super(SatinAlma, self).save(*args, **kwargs)




        


    
    def kdv_haric_alis_fiyati_hesapla(self):
        # Eğer kdvhalis_fiyati değeri girilmemişse, hata fırlat
        if self.kdvhalis_fiyati is None:
            raise ValueError("Kdv Hariç Alış Fiyatı girilmemiş.")

        # KDV'yi hesapla ve kdvhalis_fiyati'na ekle
        kdv_orani = Decimal(str(self.kdv_orani)) / 100
        return self.kdvhalis_fiyati * (1 + kdv_orani)


    def __str__(self):
        return self.stok_adi