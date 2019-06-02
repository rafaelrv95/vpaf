# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):

    fundacion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
