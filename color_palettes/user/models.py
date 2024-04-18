from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):

    first_name = models.CharField(
        "Имя",
        max_length=settings.USER_LENGTH,
        blank=False,
        validators=[
            RegexValidator(regex=settings.CHARACTER_VALIDATOR_USER)
        ]
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=settings.USER_LENGTH,
        blank=False,
        validators=[
            RegexValidator(regex=settings.CHARACTER_VALIDATOR_USER)
        ]
    )
    middle_name = models.CharField(
        "Отчество",
        max_length=settings.USER_LENGTH,
        blank=True,
        validators=[
            RegexValidator(regex=settings.CHARACTER_VALIDATOR_USER)
        ]
    )
    username = models.CharField(
        "Логин",
        max_length=64,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(regex=settings.CHARACTER_VALIDATOR_USER),
            # username_validator
        ]
    )
    password = models.CharField(
        "Пароль",
        max_length=settings.PASSWORD_LENGTH,
        blank=False,
        null=False
    )

    USERNAME_FIELD = "username"

    class Meta(AbstractUser.Meta):
        ordering = ("username",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
