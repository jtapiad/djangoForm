# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registro

# Create your views here.

class Registrar(View):
	def get(self,request):
		form = RegistroForm
		return render(request,'form.html',{'form':form})
		# return HttpResponse('')

