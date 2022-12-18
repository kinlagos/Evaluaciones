from django.contrib import admin
from .models import institucion, inscripcion

# Register your models here.
class institucionAdmin(admin.ModelAdmin):
    list_display=['id', 'nombre']

admin.site.register(institucion, institucionAdmin)

class inscripcionAdmin(admin.ModelAdmin):
    list_display=['id','nombre','fono','fecha_inscripcion', 'institucion', 'observacion']
    
admin.site.register(inscripcion, inscripcionAdmin)