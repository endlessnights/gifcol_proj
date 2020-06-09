from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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
