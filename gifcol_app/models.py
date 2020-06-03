from django.db import models
from django.conf import settings
from django.utils import timezone

# Модель Медиа-файлов
class mediamodel(models.Model):
    filetypes = (
        ('gif', 'Гифка'),
        ('video', 'Видео'),
        ('link', 'Ссылка на видео'),
        ('img', 'Картинка'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', default='root')
    title = models.CharField(null=True, blank=True, verbose_name='Название', max_length=100)
    desc = models.TextField(null=True, blank=True, verbose_name='Описание', max_length=200)
    media_gif = models.FileField(upload_to='gif/', verbose_name='Загрузка GIF', max_length=100, null=True,
                                 blank=True)
    media_video = models.FileField(upload_to='video/', verbose_name='Загрузка Видео', max_length=100, null=True,
                                 blank=True)
    media_img = models.ImageField(upload_to='img/', verbose_name='Загрузка Картинки', max_length=100,
                                   null=True,
                                   blank=True)
    medialink = models.CharField(max_length=254, verbose_name='Ссылка на видео', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата/время загрузки')
    filetype = models.CharField(max_length=254, default='gif', verbose_name='Тип записи', choices=filetypes)

    class Meta:
        verbose_name='загруженную запись'
        verbose_name_plural = 'Загруженные записи'

    def publish(self):
        self.published_date = timezone.now()
        self.save()
