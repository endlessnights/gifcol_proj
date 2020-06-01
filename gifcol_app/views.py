from django.contrib.auth import authenticate
from django.utils import timezone
from django.contrib.auth import (
    authenticate, login as built_in_login, logout as built_in_logout)
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.views.decorators.http import require_POST

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

# Login form Auth
@require_POST
def a_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        built_in_login(request, user)
        messages.success(request, 'Авторизация пройдена успешно!')
        return redirect('/')
    else:
        messages.warning(request, 'Введенные данные не верны!')
        return redirect('/')
# Logout form DeAuth
def a_logout(request):
    built_in_logout(request)
    return redirect('/')