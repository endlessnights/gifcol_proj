from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView
from django.contrib.auth import (
    authenticate, login as built_in_login, logout as built_in_logout
)

from accounts.forms import EditProfileForm, UpdateProfileForm
from accounts.models import Account


# Login form Auth
from gifcol_app.models import Meme


@require_POST
def login(request):
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
def logout(request):
    built_in_logout(request)
    return redirect('/')


def get_user_profile(request):
    imgs_added_by_user = Meme.objects.filter(
        author=request.user,
        filetype='img'
    )  # список картинок, добавленных пользователем
    gifs_added_by_user = Meme.objects.filter(
        author=request.user,
        filetype='gif'
    )  # список картинок, добавленных пользователем
    videos_added_by_user = Meme.objects.filter(
        author=request.user,
        filetype='video'
    )  # список картинок, добавленных пользователем
    return render(request, 'gifcol_app/user_profile.html', {
        "imgs_added_by_user": imgs_added_by_user,
        "gifs_added_by_user": gifs_added_by_user,
        "videos_added_by_user": videos_added_by_user,
    })


# Настройки профиля
def edit_profile(request):
    if request.method == "POST":
        current_user = request.user
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'gifcol_app/user_profile.html', {"user": current_user})
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'gifcol_app/edit_profile.html', args)


class EditUserProfileView(UpdateView):
    model = Account
    form_class = UpdateProfileForm
    template_name = "gifcol_app/update_profile.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(Account, username=self.kwargs['username'])
        return user.userprofile

    def get_success_url(self, *args, **kwargs):
        user = get_object_or_404(Account, username=self.kwargs['username'])
        return reverse('get_user_profile', args=(user,))
