from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import abstract_page, new_mediafile, logout, TagLink, bookmark_post, edit_mediafile, moderate_unpub
from accounts.views import signup

urlpatterns = [
    path('', abstract_page, name='memepage'),
    url('(?P<filetype>(gif|img|vid))', abstract_page, name='filetypepage'),
    path(r'user/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('new/', new_mediafile, name='new_mediafile'),
    path('moderate/', moderate_unpub, name='moderate_unpub'),
    path('file/<int:pk>/edit', edit_mediafile, name='edit_mediafile'),
    url(r'^signup/$', signup, name='signup'),
    url(r'(?P<id>\d+)/bookmark/$', bookmark_post, name='bookmark_post'),
    path('logout/', logout, name='logout'),
    url(r'^tag/(?P<tag_link>[a-zA-Z0-9]+)$', TagLink.as_view(), name='tag_link'),
    url(r'^\.well-known/', include('letsencrypt.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
