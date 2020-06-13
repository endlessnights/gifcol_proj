from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from accounts.models import Account
from .forms import MediaAddForm
from django.contrib.auth import logout as built_in_logout, get_user_model
from .models import Meme, Tag


# Logout form DeAuth
def logout(request):
    built_in_logout(request)
    return redirect('/')


# Страница с Гифками
def gifpage(request):
    gifmemes = Meme.objects.published().filter(
        filetype='gif',
    ).order_by(
        '-created_at'
    )
    return render(
        request,
        'gifcol_app/gifs.html',
        {
            'gifmemes': gifmemes,
            'tag_link': TagLink,
        }
    )


# Страница с видео
# Нужно еще добавить в фильтр filetype='link' - ссылка на видео и генерить youtube Iframe`ы
def videopage(request):
    videoposts = Meme.objects.filter(
        filetype='video',
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'gifcol_app/videos.html',
        {
            'videoposts': videoposts,
            'tag_link': TagLink,
        }
    )


# Страница с картинками
def imgpage(request):
    imgposts = Meme.objects.filter(
        filetype='img',
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'gifcol_app/imgs.html',
        {
            'imgposts': imgposts,
            'tag_link': TagLink
        }
    )


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


def bookmark_post(request, id):
    post = get_object_or_404(Account, id=id)
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
        return HttpResponse(status=204)
    else:
        post.bookmarks.add(request.user)
        return HttpResponse(status=204)


class TagLink(View):

    def get(self, request, tag_link):
        tag_objects = Meme.objects.filter(tags__title=tag_link)
        return render(
            request,
            'gifcol_app/tag.html',
            {
                'tag_objects': tag_objects,
                'tag_link': tag_link
            }
        )


