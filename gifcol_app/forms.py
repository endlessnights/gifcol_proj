from django import forms
from .models import Meme


class MediaAddForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = (
            'title',
            'description',
            'file',
            'filetype',
            'medialink',
            'published',
        )
class MediaEditForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = (
            'title',
            'description',
            'medialink',
            'published',
        )
