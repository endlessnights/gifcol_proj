from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .import views

urlpatterns = [
    path('', views.gifpage, name='gifpage'),
    path('video/', views.videopage, name='videopage'),
    path('img/', views.imgpage, name='imgpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)