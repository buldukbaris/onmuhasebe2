from django.db import models


class Cari(models.Model):
    cari_adi = models.CharField(max_length=255, verbose_name="Cari Adı")
    vergi_dairesi = models.CharField(max_length=255, verbose_name="Vergi Dairesi")
    vergi_no = models.CharField(max_length=20, blank=True, null=True, verbose_name="Vergi No")
    telefon = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefon")
    email = models.EmailField(blank=True, null=True, verbose_name="E-Mail")
    adres = models.TextField(blank=True, null=True, verbose_name="Adres")

    # İki seçenekli alanı ekliyoruz: Borçlu ve Alacaklı
    BORCLU = 'Borçlu'
    ALACAKLI = 'Alacaklı'

    BORC_ALACAK_CHOICES = [
        (BORCLU, 'Borçlu'),
        (ALACAKLI, 'Alacaklı'),
    ]

    cariDurum = models.CharField(
        max_length=10,
        choices=BORC_ALACAK_CHOICES,
        blank=True,
        null=True,
        help_text='Borçlu veya Alacaklı Durum Seçiniz'
    )

    Borc = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Borç Miktarı")
    Alacak = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="AlacakMiktarı")
    Bakiye = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Bakiye")

    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = "Cari"
        verbose_name_plural = "Cariler"

    def __str__(self):
        return self.cari_adi
