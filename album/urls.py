from django.conf.urls import url, include
from album.views import index, AlbumList, AlbumCreate, AlbumUpdate, AlbumDelete

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',AlbumCreate.as_view(), name='album_crear'),
    url(r'^listar$',AlbumList.as_view(), name='album_listar'),
    url(r'^editar/(?P<pk>\d+)/$',AlbumUpdate.as_view(), name='album_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',AlbumDelete.as_view(), name='album_eliminar'),
    
]
