from dataclasses import field, fields
from pyexpat import model
from django import forms 
from reservas.models import reserva


class FormReserva(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del reservante'}))
    fono=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el telefono del reservante'}))
    fechareserva=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese la fecha de la reserva'}))
    horareserva=forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'Ingrese la hora de la reserva'}))
    contpersona=forms.IntegerField(min_value=1,max_value=15,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el numero de personas'}))
    observacion=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese uns observacion'}))
    class Meta: 
        model=reserva
        fields='__all__'

    
    