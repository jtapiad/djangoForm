# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.

class Registro(models.Model):
	fechaRequerimiento = models.DateField(max_length=100, null=False, blank=False,  default=date.today)
	requerimiento = models.TextField(null=False,blank=False)
	usuario = models.CharField(max_length=100,null=False,blank=False)
	razonProblema = models.TextField()
	fechaSolucion = models.DateField(max_length=100, null=True, blank=True)
	estado = models.IntegerField(null=False,blank=False,default=0)
