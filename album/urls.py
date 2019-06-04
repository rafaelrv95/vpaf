from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required
from album.views import index, AlbumList, AlbumCreate, AlbumUpdate, AlbumDelete

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',login_required(AlbumCreate.as_view()), name='album_crear'),
    url(r'^listar$',login_required(AlbumList.as_view()), name='album_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(AlbumUpdate.as_view()), name='album_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(AlbumDelete.as_view()), name='album_eliminar'),
    
]
