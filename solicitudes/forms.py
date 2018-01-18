from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *

import datetime

ESTADOS = ( ('P','En proceso'),('T','Terminado'))

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Registro
		fields = ('fechaRequerimiento', 'requerimiento', 'usuario','razonProblema','fechaSolucion','estado')
		widgets = {
			'estado':forms.RadioSelect(choices=ESTADOS)
		}