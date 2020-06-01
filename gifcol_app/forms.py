from django import forms
from django.contrib.auth.models import User
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