from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from pedidos.views import index, PedidoCreate, PedidoList, PedidoDelete, PedidoUpdate

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^nuevo$',login_required(PedidoCreate.as_view()), name='pedidos_crear'),
    url(r'^listar$',login_required(PedidoList.as_view()), name='pedidos_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(PedidoDelete.as_view()), name='pedidos_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(PedidoUpdate.as_view()), name='pedidos_editar'),
    
    

]
