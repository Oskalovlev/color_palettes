from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator


class NameModel(models.Model):

    name = models.CharField(
        "Название",
        unique=True,
        max_length=settings.NAME_LENGTH,
        validators=[RegexValidator(
            regex=settings.CHARACTER_VALIDATOR
        )],
        null=False
    )

    class Meta:
        abstract = True


class Palette(NameModel):

    class Meta:
        verbose_name = "Палитра"
        verbose_name_plural = "Палитры"

    def __str__(self):
        return self.name


class Color(NameModel):

    hex = models.CharField(
        "HEX code",
        max_length=settings.COLOR_LENGTH,
        unique=True,
        validators=[
            RegexValidator(
                regex=settings.CHARACTER_VALIDATOR_COLOR
            )
        ]
    )

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return f"{self.hex} - {self.name}"


class ColorInPalette(models.Model):

    palette = models.ForeignKey(
        Palette,
        on_delete=models.CASCADE,
        verbose_name="Палитра",
        related_name="color_list"
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name="Цвет",
        related_name="+"
    )

    class Meta:
        ordering = ("palette",)
        verbose_name = "Цвет в палитре"
        verbose_name_plural = "Цвета в палитре"
        constraints = (
            models.UniqueConstraint(
                fields=("color", "palette",),
                name="unique_color_palette",
            ),
        )

    def __str__(self):
        return f"{self.color} в {self.palette}"
