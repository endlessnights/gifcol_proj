from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from .import views

urlpatterns = [
    path('', views.gifpage, name='gifpage'),
    path('video/', views.videopage, name='videopage'),
    path('img/', views.imgpage, name='imgpage'),
    path('login/', views.a_login, name='a_login'),
    path('logout/', views.a_logout, name='a_logout'),
    path('new/', views.new_mediafile, name='new_mediafile'),
    url(r'user/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name='get_user_profile'),
    url(r'^user/settings/$', views.edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)