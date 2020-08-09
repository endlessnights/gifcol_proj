from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView
from django.contrib.auth import (
    authenticate, login as built_in_login, logout as built_in_logout, get_user_model
)

from accounts.forms import EditProfileForm, UpdateProfileForm, SignUpForm
from accounts.models import Account


# Login form Auth
from gifcol_app.models import Meme

@require_POST
def register(request):
    username = request.POST.get('usernamereg')
    password = request.POST.get('passwordreg')
    password1 = request.POST.get('password1')

    if not any(
        [username, password, password1]
    ):
        return JsonResponse(
            {'message': 'Form incorrect'}
        )

    if not password or not password1:
        return JsonResponse(
            {'message': 'Empty password'}
        )

    if password != password1:
        return JsonResponse(
            {'message': 'passwords did not match'}
        )
    user_model = get_user_model()

    if user_model.objects.filter(username=username).first():
        return JsonResponse(
            {'message': 'User exists'}
        )

    user = user_model.objects.create_user(
        username=username,
        password=password
    )

    user.save()

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


def get_user_profile(request, username):
    #получаеми имя пользователя из url
    userprofile = Account.objects.get(username=username)
    #список гифок, добавленных конкретным пользователем
    imgs_added_by_user = Meme.objects.filter(
        author=userprofile,
        filetype='img'
    )  # список картинок, добавленных пользователем
    gifs_added_by_user = Meme.objects.filter(
        author=userprofile,
        filetype='gif'
    )  # список картинок, добавленных пользователем
    videos_added_by_user = Meme.objects.filter(
        author=userprofile,
        filetype='video'
    )  # список картинок, добавленных пользователем
    return render(request, 'accounts/user_profile.html', {
        "user": userprofile,
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
            return render(request, 'accounts/user_profile.html', {"user": current_user})
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


class EditUserProfileView(UpdateView):
    model = Account
    form_class = UpdateProfileForm
    template_name = "accounts/update_profile.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(Account, username=self.kwargs['username'])
        return user

    def get_success_url(self, *args, **kwargs):
        user = get_object_or_404(Account, username=self.kwargs['username'])
        return reverse('get_user_profile', args=(user,))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})