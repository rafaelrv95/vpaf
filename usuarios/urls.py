from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from usuarios.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar',staff_member_required(login_required(RegistroUsuario.as_view())), name='registrar'),
    
]