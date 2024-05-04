# Generated by Django 4.2.9 on 2024-02-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Satis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stok_adi", models.CharField(max_length=255, verbose_name="Stok Adı")),
                (
                    "stok_kodu",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="Stok Kodu",
                    ),
                ),
                (
                    "barkod",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="Barkod",
                    ),
                ),
                (
                    "miktar",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Miktar"
                    ),
                ),
                (
                    "birimi",
                    models.CharField(
                        default="adet", max_length=255, verbose_name="Birimi"
                    ),
                ),
                (
                    "kdv_orani",
                    models.CharField(
                        default="20", max_length=20, verbose_name="Kdv Oranı"
                    ),
                ),
                (
                    "kdvhsatis_fiyati",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Kdv Hariç Satış Fiyatı",
                    ),
                ),
                (
                    "kdvdsatis_fiyati",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Kdv Dahil Satış Fiyatı",
                    ),
                ),
                ("cari_adi", models.CharField(max_length=255, verbose_name="Cari Adı")),
                (
                    "tutari_kdvharic",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=15,
                        null=True,
                        verbose_name="Tutar (KDV Hariç)",
                    ),
                ),
                (
                    "tutari_kdvdahil",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=15,
                        null=True,
                        verbose_name="Tutar (KDV Dahil)",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "kdv_dahil",
                    models.BooleanField(default=True, verbose_name="KDV Dahil Mi"),
                ),
            ],
        ),
    ]
