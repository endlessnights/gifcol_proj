from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import gifpage, new_mediafile, videopage, imgpage, bookmark_post, logout, tag_link

urlpatterns = [
    path('', gifpage, name='gifpage'),
    path(r'user/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('new/', new_mediafile, name='new_mediafile'),
    path('video/', videopage, name='videopage'),
    path('img/', imgpage, name='imgpage'),
    path('file/<int:pk>/bookmark_post/', bookmark_post, name='bookmark_post'),
    path('logout/', logout, name='logout'),
    url(r'^tag/(?P<tag_link>[a-zA-Z0-9]+)$', tag_link.as_view(), name='tag_link'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
