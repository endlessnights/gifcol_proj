from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Account

class ReigsterNewUser(UserChangeForm):
    class Meta:
        model = User
        fields=(
            'username',
            'password',
        )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            'description',
            'website',
            'vksite',
            'fbsite',
            'avatar',
            'cover',
        )

    def save(self, user=None):
        user_profile = super(UpdateProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )