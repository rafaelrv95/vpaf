from django.conf.urls import url
from usuarios.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar',RegistroUsuario.as_view(), name='registrar'),
    
]