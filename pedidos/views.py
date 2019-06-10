# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from pedidos.forms import PedidoForm
from pedidos.models import Pedido
from album.models import Album

from django.template.defaulttags import register

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
        
        ###### total en estado de entregado#############
        context['cantidad_total']= cantidad

        suma=0
        for i in cantidad:
            if i.estado =="entregado":
                suma = suma+int(i.cantidad)
        context['cantidad_total']= suma
  ###################### fin total#################


  ############# total menos la cantidad de entregados ##################
        
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



        
        albumTotal= Album.objects.all()
        context['album_total']=albumTotal
        salbum = 0
        for i in cantalbum:
            salbum = salbum+int(i.cantidad)
        context['album_total']=salbum 





        return context    

class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedidos_form.html'
    success_url = reverse_lazy('pedidos:pedidos_listar')




    def get_context_data(self, **kwargs):
        context =super(PedidoCreate, self).get_context_data(**kwargs)
    

    ##################### combobox ############


        
        listarAlbum= Album.objects.all()
        context['listar_album']=listarAlbum

        return context
        


####################


class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedidos/pedidos_delete.html'
    success_url = reverse_lazy('pedidos:pedidos_listar')


###### actualizar la cantidad de pedidos al eliminar un con estado entregado

    def get_context_data(self, **kwargs):
        context =super(PedidoDelete, self).get_context_data(**kwargs)
    

    


        
        
        funda = Pedido.objects.get(pk=self.kwargs.get('pk')).album_p
        pedido_cant = Pedido.objects.get(pk=self.kwargs.get('pk')).cantidad
        pedido_estado = Pedido.objects.get(pk=self.kwargs.get('pk')).estado
        cant_album = Album.objects.get(fundacion = funda).cantidad
        if pedido_estado == "entregado":
            Album.objects.filter(fundacion = funda).update(cantidad = cant_album-pedido_cant)



        return context
        

class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedidos/pedidos_form.html'
    success_url = reverse_lazy('pedidos:pedidos_listar')

    def get_context_data(self, **kwargs):
        context =super(PedidoUpdate, self).get_context_data(**kwargs)
    

    ##################### combobox ############


        
        listarAlbum= Album.objects.all()
        context['listar_album']=listarAlbum

        return context
