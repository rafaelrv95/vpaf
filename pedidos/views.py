# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from pedidos.forms import PedidoForm
from pedidos.models import Pedido
from album.models import Album
# Create your views here.

def index(request):
    return render(request, 'pedidos/index.html')

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

class PedidoList(ListView):
    model = Pedido
    template_name = 'pedidos/pedidos_list.html'

     
    def get_context_data(self, **kwargs):
        context =super(PedidoList, self).get_context_data(**kwargs)
        cantidad = Pedido.objects.all()
        
        ###### total #############
        context['cantidad_total']= cantidad

        suma=0
        for i in cantidad:
            if i.estado =="entregado":
                suma = suma+int(i.cantidad)
        context['cantidad_total']= suma
  ###################### fin total#################


  ############# album ##################
        
        cantalbum= Album.objects.all()
        context['cantidad_album']=cantalbum
        sumalbum = 0
        for i in cantalbum:
            sumalbum = sumalbum+int(i.cantidad)
        context['cantidad_album']=sumalbum - suma




  ########################################


##### total de pedidos en la tabla ############
        
        totaltabla= Pedido.objects.all()
        context['total_tabla']=totaltabla
        sumaTabla = 0
        for i in totaltabla:
            sumaTabla = sumaTabla+int(i.cantidad)
        context['total_tabla']=sumaTabla

###########################################################


        return context
    

class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedidos_form.html'
    success_url = reverse_lazy('pedidos:pedidos_listar')

class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedidos/pedidos_delete.html'
    success_url = reverse_lazy('pedidos:pedidos_listar')

class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedidos_form.html'
    success_url = reverse_lazy('pedidos:pedidos_listar')
