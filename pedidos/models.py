# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pedido(models.Model):
    
    responsable = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    album_p = models.CharField(max_length=150)
    fecha = models.DateField()
    contacto = models.CharField(max_length=150)
    estado = models.CharField(max_length=250)
    observaciones = models.CharField(max_length=250)
    
    def __unicode__(self):
        return '{}'.format(self.responsable)