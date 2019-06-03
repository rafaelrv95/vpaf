# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from album.forms import AlbumForm
from album.models import Album
# Create your views here.

def index(request):
    return render(request, 'album/index.html')


def album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('album:index')
    else:
        form = AlbumForm()
    return render(request, 'album/album_form.html', {'form':form})

def album_list(request):
    album = Album.objects.all()
    contexto = {'album':album}
    return render(request, 'album/album_list.html', contexto)