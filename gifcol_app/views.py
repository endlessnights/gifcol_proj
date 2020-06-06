from django.http import HttpResponse
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MediaAddForm

from .models import Meme


# Страница с Гифками
def gifpage(request):
    gifmemes = Meme.objects.published().filter(
        filetype='gif',
    ).order_by(
        '-created_at'
    )
    return render(request, 'gifcol_app/gifs.html', {'memes': gifmemes})


# Страница с видео
# Нужно еще добавить в фильтр filetype='link' - ссылка на видео и генерить youtube Iframe`ы
def videopage(request):
    videoposts = Meme.objects.filter(
        filetype='video',
    ).order_by(
        '-created_at'
    )
    return render(request, 'gifcol_app/videos.html', {'videoposts': videoposts})


# Страница с картинками
def imgpage(request):
    imgposts = Meme.objects.filter(
        filetype='img',
    ).order_by(
        '-created_at'
    )
    return render(request, 'gifcol_app/imgs.html', {'imgposts': imgposts})


# Загрузить новый файл
def new_mediafile(request):
    if request.method == "POST":
        form = MediaAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
        return redirect('/')
    else:
        form = MediaAddForm()
    return render(request, 'gifcol_app/edit.html', {'form': form})


def bookmark_post(request, pk):
    is_bookmarked = False
    post = get_object_or_404(Meme, pk=pk)
    if post.bookmark.filter(pk=request.user.id).exists():
        post.bookmark.remove(request.user)
        is_bookmarked = False
    else:
        post.bookmark.add(request.user)
        is_bookmarked = True
    return HttpResponse(status=204)
