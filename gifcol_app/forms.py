from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import mediamodel

class MediaAddForm(forms.ModelForm):
    class Meta:
        model = mediamodel
        fields = (
            'title',
            'desc',
            'media_gif',
            'media_video',
            'media_img',
            'medialink',
            'filetype',
        )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )