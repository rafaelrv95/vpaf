from django.conf.urls import url, include
from album.views import index, album_view, album_list,album_edit, album_delete, AlbumList, AlbumCreate

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',AlbumCreate.as_view(), name='album_crear'),
    url(r'^listar$',AlbumList.as_view(), name='album_listar'),
    url(r'^editar/(?P<id_album>\d+)/$',album_edit, name='album_editar'),
    url(r'^eliminar/(?P<id_album>\d+)/$',album_delete, name='album_eliminar'),
    
]
