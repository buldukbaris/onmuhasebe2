# Generated by Django 4.2.9 on 2024-03-06 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sakiz", "0007_remove_sakizmakinesi_bolge_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="sakizmakinesi", name="cari",),
    ]
