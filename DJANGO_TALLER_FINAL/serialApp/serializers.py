from rest_framework import serializers
from serialApp.models import inscripcion, institucion
from django import forms

class inscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model=inscripcion
        fields = '__all__'

class institucionSerializer(serializers.ModelSerializer):
    class Meta:
        model=institucion
        fields = '__all__'
        