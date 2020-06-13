from django.db import models
from django.conf import settings

from gifcol_proj.base_models import TimeStamped, PublishedModel


class Tag(TimeStamped, PublishedModel):
    title = models.CharField(
        verbose_name='Название',
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Meme(TimeStamped, PublishedModel):
    filetypes = (
        ('gif', 'Гифка'),
        ('video', 'Видео'),
        # ('link', 'Ссылка на видео'),
        ('img', 'Картинка'),
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        default=0,
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=100,
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=200
    )
    file = models.FileField(
        upload_to='file/',
        verbose_name='Файл',
    )
    filetype = models.CharField(
        max_length=254,
        default='img',
        verbose_name='Тип записи',
        choices=filetypes
    )
    medialink = models.CharField(
        max_length=254,
        verbose_name='Ссылка на видео',
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        related_name='memes',
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Загруженную запись'
        verbose_name_plural = 'Загруженные записи'
