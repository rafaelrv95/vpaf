# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from album.forms import AlbumForm
from album.models import Album

from pedidos.models import Pedido
# Create your views here.
from django.template.defaulttags import register
def index(request):
    return render(request, 'album/index.html')

'''
def album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('album:album_listar')
    else:
        form = AlbumForm()
    return render(request, 'album/album_form.html', {'form':form})

def album_list(request):
    album = Album.objects.all().order_by('id')
    contexto = {'album':album}
    return render(request, 'album/album_list.html', contexto)

def album_edit(request, id_album):
    album = Album.objects.get(id=id_album)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
        return redirect('album:album_listar')
    return render(request, 'album/album_form.html',{'form':form})

def album_delete(request, id_album):
    album = Album.objects.get(id=id_album)
    if request.method == 'POST':
        album.delete()
        return redirect('album:album_listar')
    return render(request, 'album/album_delete.html',{'album':album})
'''
class AlbumList(ListView):
    model = Album
    template_name = 'album/album_list.html'
    

    def get_context_data(self, **kwargs):
        context =super(AlbumList, self).get_context_data(**kwargs)
    
        @register.filter
        def get_item(dictionary, key):
            return dictionary.get(key)


    ##################### entregados ############

        entregados = Pedido.objects.all()
        context['cantidad_enpedido']= entregados
        fundacion = [] # nombre de la fundacion
        entrega = [] # entregados de cada fundacion -- depende del estado --
    
        for ent in entregados:
            if ent.estado == "entregado":
                fundacion.append(ent.album_p)
                entrega.append(ent.cantidad)

        dicc_entregados = list(zip(fundacion, entrega)) # los duplicados se agrpan y su cantidad se suma
        resultado = {}

        for k, v in dicc_entregados:
            total = resultado.get(k, 0) + v
            resultado[k] = total
        context['en_album']= resultado

        return context
        


####################


class AlbumCreate(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/album_form.html'
    success_url = reverse_lazy('album:album_listar')

class AlbumUpdate(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/album_form.html'
    success_url = reverse_lazy('album:album_listar')

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'album/album_delete.html'
    success_url = reverse_lazy('album:album_listar')