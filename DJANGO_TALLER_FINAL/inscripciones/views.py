from django.shortcuts import render, redirect
import requests
from serialApp.models import institucion, inscripcion
from .forms import FormInscripcion, FormInstitucion
# Create your views here.

def index(request):
    return render(request, 'index.html')

def inscripciones(request):
    response=requests.get('http://localhost:8000/inscripcionesApi/')
    inscripciones=response.json()
    contex={'inscripciones':inscripciones}
    return render(request, 'inscripciones.html', contex)

def instituciones(request):
    response=requests.get('http://localhost:8000/institucionesApi/')
    instituciones=response.json()
    contex={'instituciones': instituciones}
    return render(request, 'instituciones.html', contex)


def agregarInstitucion(request):
    form=FormInstitucion()
    if request.method=='POST':
        form=FormInstitucion(request.POST)
        if form.is_valid():
            form.save()
        return instituciones(request)
    data={'form':form}
    return render(request, 'agregar_institucion.html', data)

def eliminarInstitucion(request, id):
    pro= institucion.objects.get(id=id)
    pro.delete()
    return redirect('instituciones')

def actualizarInstitucion(request, id):
    pro=institucion.objects.get(id=id)
    form=FormInstitucion(instance=pro)
    if request.method=='POST':
        form=FormInstitucion(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return instituciones(request)
    data={'form':form}
    return render(request, 'agregar_institucion.html', data)


def agregarInscripcion(request):
    formIn=FormInscripcion()
    if request.method=='POST':
        formIn=FormInscripcion(request.POST)
        if formIn.is_valid():
            formIn.save()
        return inscripciones(request)
    data={'formIn':formIn}
    return render(request, 'agregar_inscripcion.html', data)

def eliminarInscripcion(request, id):
    pro=inscripcion.objects.get(id=id)
    pro.delete()
    return redirect('inscripciones')

def actualizarInscripcion(request, id):
    pro=inscripcion.objects.get(id=id)
    formIn=FormInscripcion(instance=pro)
    if request.method=='POST':
        formIn=FormInscripcion(request.POST, instance=pro)
        if formIn.is_valid():
            formIn.save()
        return inscripciones(request)
    data={'formIn':formIn}
    return render(request, 'agregar_inscripcion.html', data)
    