from django.db import models

# Create your models here.
"""
inscripcion=[
    ('RESERVADO','RESERVADO'),
    ('COMPLETADA','COMPLETADA'),
    ('ANULADA','ANULADA'),
    ('NO ASISTEN', 'NO ASISTEN'),
]

class inscripcion(models.Model):
    nombre=models.CharField(max_length=50)
    fono = models.CharField(max_length=20)
    fecha = models.DateField()
    institucion= models.CharField(max_length=30)
    hora=models.TimeField()
    estado=models.CharField( 
        max_length=20,
        null=False, blank=False,
        choices=inscripcion)
    def __str__(self):
        return self
    observacion=models.CharField(max_length=200)
"""
    