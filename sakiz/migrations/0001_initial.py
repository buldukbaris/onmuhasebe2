# Generated by Django 4.2.9 on 2024-03-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SakizMakinesi",
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
                ("marka", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
        ),
    ]