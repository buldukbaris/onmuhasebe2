# Generated by Django 4.2.9 on 2024-03-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sakiz", "0005_alter_sakizmakinesi_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sakizmakinesi",
            name="aciklama",
            field=models.CharField(
                blank=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="Açıklama",
            ),
        ),
        migrations.AlterField(
            model_name="sakizmakinesi",
            name="bolge",
            field=models.CharField(
                blank=True, default="", max_length=255, null=True, verbose_name="Bölge"
            ),
        ),
        migrations.AlterField(
            model_name="sakizmakinesi",
            name="makineNo",
            field=models.CharField(
                blank=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="Makine No",
            ),
        ),
    ]
