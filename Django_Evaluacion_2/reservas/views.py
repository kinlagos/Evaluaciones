from django.shortcuts import render, redirect
from reservas.forms import FormReserva

from reservas.models import reserva

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoReservas(request):
    reservas = reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_reserva.html', data)

def eliminarReserva(request, id):
    pro = reserva.objects.get(id = id)
    pro.delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    pro = reserva.objects.get(id = id)
    form = FormReserva(instance=pro)
    if request.method == 'POST':
        form = FormReserva(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_reserva.html', data)