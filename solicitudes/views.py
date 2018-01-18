# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404
from .forms import RegistroForm
from solicitudes.models import Registro
from django.contrib import messages

# Create your views here.

# class Registrar(View):
# 	def get(self,request):
# 		form = RegistroForm()
# 		return render(request,'form.html',{'form':form})
	
# 	def post(self,request):
# 		form = RegistroForm(request.POST or None)
# 		success = False
# 		if form.is_valid():
# 			form.save()
# 			form = RegistroForm()
# 			success = True
# 		messages.success(request, 'Profile details updated.')
# 		return render(request,'form.html',{'form':form})

# class ListadoRegistros(View):
# 	def get(self,request):
# 		return render(request,'listado.html',{'listado':Registro.objects.all()})
	
# 	def delete(self,request):
# 		print "osoooo"
# 		return redirect('listado.html')

# class eliminar(DeleteView):
# 	def get_object(self, queryset=None):
# 		return redirect("/lista")


# class EditarRegistro(View):
# 	def get(self,request,*args, **kwargs):
# 		registro = Registro.objects.get(id=kwargs["id"])
# 		form = RegistroForm(instance=registro)
# 		return render(request,'form.html',{'form':form})

# 	def post(self,request,*args, **kwargs):
# 		form = RegistroForm(request.POST,instance=Registro.objects.get(id=kwargs["id"]))
# 		success = False
# 		if form.is_valid():
# 			form.save()
# 			success = True
# 			messages.success(request, 'Registro Actualizado')
# 			return render(request,'form.html',{'form':form})
# 		else:
# 			messages.error(request, 'Error en la actualizacion')
# 			return render(request,'form.html',{'form':RegistroForm()})
# 			

#class based views

class RegistroList(ListView):
	model = Registro

class RegistroCrear(CreateView):
	model = Registro
	fields = ['fechaRequerimiento','requerimiento','usuario','razonProblema','fechaSolucion','estado']
	success_url = reverse_lazy('registro_list')

class RegistroUpdate(UpdateView):
	model = Registro
	fields = ['fechaRequerimiento','requerimiento','usuario','razonProblema','fechaSolucion','estado']
	success_url = reverse_lazy('registro_list')

class RegistroDelete(DeleteView):
	model = Registro
	success_url = reverse_lazy('registro_list')

def eliminarRegistro(request,pk):
	# Registro.objects.get(pk=pk)
	registro = get_object_or_404(Registro,pk=pk)
	registro.delete()
	return redirect('registro_list')
