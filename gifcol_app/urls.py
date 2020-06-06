from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import gifpage, new_mediafile, videopage, imgpage, bookmark_post

urlpatterns = [
    path('', gifpage, name='gifpage'),
    path(r'accounts', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('new/', new_mediafile, name='new_mediafile'),
    path('video/', videopage, name='videopage'),
    path('img/', imgpage, name='imgpage'),
    path('file/<int:pk>/bookmark_post/', bookmark_post, name='bookmark_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
