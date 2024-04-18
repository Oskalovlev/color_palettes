# Generated by Django 5.0.4 on 2024-04-17 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("palette", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="color",
            name="palette",
        ),
        migrations.CreateModel(
            name="ColorInPalette",
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
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="palette.color",
                    ),
                ),
                (
                    "palette",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="palettes",
                        to="palette.palette",
                    ),
                ),
            ],
            options={
                "verbose_name": "Цвет в палитре",
                "verbose_name_plural": "Цвета в палитре",
            },
        ),
        migrations.AddConstraint(
            model_name="colorinpalette",
            constraint=models.UniqueConstraint(
                fields=("color", "palette"), name="unique_color_palette"
            ),
        ),
    ]