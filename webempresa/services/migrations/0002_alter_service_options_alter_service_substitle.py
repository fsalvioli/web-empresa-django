# Generated by Django 4.2.4 on 2023-10-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="service",
            options={
                "ordering": ["-created"],
                "verbose_name": "servicio",
                "verbose_name_plural": "servicios",
            },
        ),
        migrations.AlterField(
            model_name="service",
            name="substitle",
            field=models.CharField(max_length=200, verbose_name="Subtítulo"),
        ),
    ]
