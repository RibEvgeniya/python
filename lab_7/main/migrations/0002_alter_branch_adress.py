# Generated by Django 5.0.4 on 2024-04-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="adress",
            field=models.CharField(max_length=120, verbose_name="Адрес"),
        ),
    ]
