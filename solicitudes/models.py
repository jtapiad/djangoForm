# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.

ESTADOS = ( ('P','En proceso'),('T','Terminado'))

class Registro(models.Model):
	fechaRequerimiento = models.DateField(max_length=100, null=False, blank=False,  default=date.today)
	requerimiento = models.TextField(null=False,blank=False)
	usuario = models.CharField(max_length=100,null=True,blank=True)
	razonProblema = models.TextField(blank=True)
	fechaSolucion = models.DateField(max_length=100, null=True, blank=True)
	estado = models.CharField(max_length=1,null=False,blank=False,choices=ESTADOS)

	def __unicode__(self):
		return self.requerimiento

	def get_absolute_url(self):
		return reverse('registro_edit',kwargs={'pk':self.pk})