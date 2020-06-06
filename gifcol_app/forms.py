from django import forms
from .models import Meme


class MediaAddForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = (
            'title',
            'description',
            'file',
            'medialink',
        )