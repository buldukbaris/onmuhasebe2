# Generated by Django 4.2.9 on 2024-03-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cariler", "0002_alter_cari_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="cari",
            name="caridurum",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Cari Durum"
            ),
        ),
    ]
