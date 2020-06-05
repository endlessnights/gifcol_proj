from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import mediamodel, UserProfile


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
            'password',
        )


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = (
            'userdesc',
            'userwebsite',
            'avatar',
            'cover',
        )

    def save(self, user=None):
        user_profile = super(UpdateProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile
