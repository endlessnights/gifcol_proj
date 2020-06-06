from django.contrib.auth.models import AbstractUser
from django.db import models

from gifcol_app.models import Meme
from gifcol_proj.base_models import TimeStamped


class Account(AbstractUser, TimeStamped):
    description = models.TextField(
        max_length=250,
        verbose_name='Обо мне',
        null=True,
        blank=True,
    )
    website = models.URLField(
        verbose_name='Мой вебсайт',
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        upload_to='profiles_images',
        blank=True,
        verbose_name='Аватар',
    )
    cover = models.ImageField(
        upload_to='covers',
        blank=True,
        verbose_name='Обложка',
    )

    bookmarks = models.ManyToManyField(
        Meme,
        verbose_name='Избранное',
        related_name='users_bookmarked'
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
