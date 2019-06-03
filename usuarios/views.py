# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from usuarios.forms import RegistroForm

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuarios/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('album:album_listar')
