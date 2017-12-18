from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('fechaRequerimiento','requerimiento','usuario','razonProblema','fechaSolucion','estado')

class NuevoRegistro(RegistroForm):
	 def __init__(self, *args, **kwargs):
	 	self.fields['fechaSolicitud'] = forms.DateField()