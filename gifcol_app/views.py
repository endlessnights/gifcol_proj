from django.db.models import Case, When, Value, BooleanField
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from accounts.models import Account
from .forms import MediaAddForm, MediaEditForm
from django.contrib.auth import logout as built_in_logout, get_user_model
from .models import Meme, Tag


# Logout form DeAuth
def logout(request):
    built_in_logout(request)
    return redirect('/')


def abstract_page(request, filetype=None):
    bookmarks = request.user.bookmarks.values_list('id', flat=True) if request.user.is_authenticated else [0]
    memes = Meme.objects.published().filter(
#        filetype=filetype or 'gif',
    ).order_by(
        'created_at'
    )[:10] .annotate(
        bookmarked=Case(
            When(
                id__in=bookmarks,
                then=Value(True),
            ),
            default=Value(False),
            output_field=BooleanField(),
        )
    )
    tags = Tag.objects.published().filter()
    return render(
        request,
        'gifcol_app/memes_base.html',
        {
            'memes': memes,
            'tags': tags,
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


def edit_mediafile(request, pk):
    post = get_object_or_404(Meme, pk=pk)
    if request.method == "POST":
        form = MediaEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at = timezone.now()
            post.save()
        return redirect('/')
    else:
        form = MediaEditForm(instance=post)
    return render(request, 'gifcol_app/edit_mediafile.html', {'form': form})


def bookmark_post(request, id):
    if request.user.bookmarks.filter(id=id):
        request.user.bookmarks.remove(id)
        return HttpResponse(status=204)
    else:
        request.user.bookmarks.add(id)
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


def moderate_unpub(request):
    memes = Meme.objects.filter(published=False,
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'gifcol_app/memes_base.html',
        {
            'memes': memes,
        }
    )

def search_posts(request):
    bookmarks = request.user.bookmarks.values_list('id', flat=True) if request.user.is_authenticated else [0]
    query = request.GET.get('q')
    memes = Meme.objects.published().filter(Q(title__icontains=query) | Q(tags__title=query)).order_by(
        'created_at'
    ).annotate(
        bookmarked=Case(
            When(
                id__in=bookmarks,
                then=Value(True),
            ),
            default=Value(False),
            output_field=BooleanField(),
        )
    ).distinct()

    return render(
        request,
        'gifcol_app/search_results.html',
        {
            'memes': memes,
            'query': query,
        }
    )