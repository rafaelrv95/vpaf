# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pedido(models.Model):
    
    responsable = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    contacto = models.CharField(max_length=150)
    observaciones = models.CharField(max_length=250)
    
