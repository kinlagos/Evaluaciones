from django import forms
from serialApp.models import inscripcion, institucion


class FormInscripcion(forms.ModelForm):
    id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el id del inscriptor'}))
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del inscriptor'}))
    fono=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el telefono del inscriptor'}))
    fecha_inscripcion=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese la fecha de la inscripcion(año-mes-dia)'}))
    institucion=forms.ModelChoiceField(queryset=institucion.objects.all())
    observacion=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese uns observacion'}))
    class Meta: 
        model=inscripcion
        fields='__all__'

#nombre_variable = forms.ModelChoiceField(queryset=nombre_modelo.objects.all())

class FormInstitucion(forms.ModelForm):
    id=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el id de la institucion'}))
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre de la institucion'}))
    class Meta:
        model=institucion
        fields='__all__'
    