from django.conf.urls import url
from django.urls import path

from accounts.views import (
    get_user_profile, edit_profile, EditUserProfileView, logout, login
)


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    url(r'(?P<username>[a-zA-Z0-9]+)$', get_user_profile, name='get_user_profile'),
    url(r'^edit/$', edit_profile, name='edit_profile'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/update/$', EditUserProfileView.as_view(), name='update_profile'),
]
