from django.conf.urls import url, include
from album.views import index, album_view, album_list,album_edit, album_delete

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',album_view, name='album_crear'),
    url(r'^listar$',album_list, name='album_listar'),
    url(r'^editar/(?P<id_album>\d+)/$',album_edit, name='album_editar'),
    url(r'^eliminar/(?P<id_album>\d+)/$',album_delete, name='album_eliminar'),
    
]
