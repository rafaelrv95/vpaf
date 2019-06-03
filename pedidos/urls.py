from django.conf.urls import url, include
from pedidos.views import index, PedidoCreate, PedidoList, PedidoDelete, PedidoUpdate

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',PedidoCreate.as_view(), name='pedidos_crear'),
    url(r'^listar$',PedidoList.as_view(), name='pedidos_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$',PedidoDelete.as_view(), name='pedidos_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$',PedidoUpdate.as_view(), name='pedidos_editar'),
    
    

]
