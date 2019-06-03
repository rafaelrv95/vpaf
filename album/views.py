# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from album.forms import AlbumForm
from album.models import Album
# Create your views here.

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