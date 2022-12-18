from django.db import models

# Create your models here.
inscrip=[
    ('RESERVADO','RESERVADO'),
    ('COMPLETADA','COMPLETADA'),
    ('ANULADA','ANULADA'),
    ('NO ASISTEN', 'NO ASISTEN'),
]

class institucion(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre 

class inscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    fono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateTimeField(auto_now=True, blank=True)
    institucion= models.ForeignKey(institucion, on_delete=models.CASCADE)
    estado=models.CharField( 
        max_length=20,
        null=False, blank=False,
        choices=inscrip)
    def __str__(self):
        return self
    observacion=models.CharField(max_length=200, blank=True)

    