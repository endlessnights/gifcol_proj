from django.db import models

from gifcol_proj.base_managers import PublishedManager


class TimeStamped(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    class Meta:
        abstract = True


class PublishedModel(models.Model):

    objects = PublishedManager()

    published = models.BooleanField(verbose_name='Опубликовано', default=False)

    class Meta:
        abstract = True
