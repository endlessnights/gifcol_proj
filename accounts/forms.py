from django.contrib.auth.forms import UserChangeForm

from accounts.models import Account


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
            'avatar',
            'cover',
        )

    def save(self, user=None):
        user_profile = super(UpdateProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile
