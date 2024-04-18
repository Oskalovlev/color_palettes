# Generated by Django 5.0.4 on 2024-04-17 10:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Palette",
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
                    "name",
                    models.CharField(
                        max_length=256,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^[а-яА-ЯёЁa-zA-Z0-9]+$"
                            )
                        ],
                        verbose_name="Название",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Color",
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
                    "name",
                    models.CharField(
                        max_length=256,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^[а-яА-ЯёЁa-zA-Z0-9]+$"
                            )
                        ],
                        verbose_name="Название",
                    ),
                ),
                (
                    "hex",
                    models.CharField(
                        max_length=7,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^#([0-9a-fA-F]{3,6})$"
                            )
                        ],
                        verbose_name="HEX code",
                    ),
                ),
                (
                    "palette",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="colors",
                        to="palette.palette",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
