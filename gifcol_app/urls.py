from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .import views

urlpatterns = [
    path('', views.gifpage, name='gifpage'),
    path('video/', views.videopage, name='videopage'),
    path('img/', views.imgpage, name='imgpage'),
    path('login/', views.a_login, name='a_login'),
    path('logout/', views.a_logout, name='a_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)