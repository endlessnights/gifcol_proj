from django.utils import timezone

from django.shortcuts import render

# Create your views here.
from .models import mediamodel

#Страница с Гифками
def gifpage(request):
    gifposts = mediamodel.objects.filter(filetype='gif', created_date__lte=timezone.now()).order_by('created_date').reverse()
    return render(request, 'app/gifs.html',
                  {
                      'gifposts': gifposts
                  })
#Страница с видео
#Нужно еще добавить в фильтр filetype='link' - ссылка на видео и генерить youtube Iframe`ы
def videopage(request):
    videoposts = mediamodel.objects.filter(filetype='video', created_date__lte=timezone.now()).order_by('created_date').reverse()
    return render(request, 'app/videos.html',
                  {
                      'videoposts': videoposts
                  })
#Страница с картинками
def imgpage(request):
    imgposts = mediamodel.objects.filter(filetype='img', created_date__lte=timezone.now()).order_by('created_date').reverse()
    return render(request, 'app/imgs.html',
                  {
                      'imgposts': imgposts
                  })