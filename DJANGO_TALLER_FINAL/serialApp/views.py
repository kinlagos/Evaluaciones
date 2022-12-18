from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from .models import institucion, inscripcion
from .serializers import inscripcionSerializer, institucionSerializer
from rest_framework.decorators import api_view

class listarInscripciones(APIView):
    def get(self, request):
        Inscripcion= inscripcion.objects.all()
        serial= inscripcionSerializer(Inscripcion, many=True)
        return Response(serial.data)

    def post(self, request):
        serial= inscripcionSerializer(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class datosInscripcion(APIView):
    def get_object(self, pk):
        try:
            return inscripcion.objects.get(id=pk)
        except inscripcion.DoesNotExist:
            return Http404

    def get(self, request, pk):
        Inscripcion= self.get_object(pk)
        serial=inscripcionSerializer(Inscripcion)
        return Response(serial.data)

    def put(self, request, pk):
        Inscripcion= self.get_object(pk)
        serial= inscripcionSerializer(Inscripcion, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Inscripcion= self.get_object(pk)
        Inscripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def lista_institucion(request):
    if request.method=='GET':
        Institucion=institucion.objects.all()
        serial=institucionSerializer(Institucion, many=True) 
        return Response(serial.data)

    if request.method=='POST':
        serial=institucionSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_institucion(request, id):
    try:
        Institucion=institucion.objects.get(pk=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=institucionSerializer(Institucion)
        return Response(serial.data)

    if request.method=='PUT':
        serial=institucionSerializer(Institucion, data=request.data)
        if serial.is_valid():
            serial.save() 
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        Institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)