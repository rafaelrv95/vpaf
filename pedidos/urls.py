from django.conf.urls import url, include
from pedidos.views import index_pedido

urlpatterns = [
    url(r'^index$', index_pedido),
]
