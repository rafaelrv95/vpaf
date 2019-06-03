from django.conf.urls import url, include
from album.views import index, album_view, album_list

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',album_view, name='album_crear'),
    url(r'^listar$',album_list, name='album_listar'),
    
]
