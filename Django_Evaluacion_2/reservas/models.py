from random import choices
from django.db import models

reserva=[
    ('RESERVADO','RESERVADO'),
    ('COMPLETADA','COMPLETADA'),
    ('ANULADA','ANULADA'),
    ('NO ASISTEN', 'NO ASISTEN'),
]
# Create your models here.
class reserva(models.Model):
    nombre=models.CharField(max_length=50)
    fono = models.CharField(max_length=20)
    fechareserva = models.DateField()
    horareserva=models.TimeField()
    contpersona=models.IntegerField()
    estado=models.CharField( 
        max_length=20,
        null=False, blank=False,
        choices=reserva)
    def __str__(self):
        return self
    observacion=models.CharField(max_length=200)

    