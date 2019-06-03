from django.conf.urls import url, include
from album.views import index, album_view

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',album_view, name='album_crear'),
]
