"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inscripciones import views as inscripcionesViews
from serialApp import views as serialAppViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inscripcionesViews.index, name='index'),
    path('inscripcionesApi/', serialAppViews.listarInscripciones.as_view(), name='inscripcionesApi'),
    path('inscripcionesApi/<int:id>', serialAppViews.datosInscripcion.as_view(), name='inscripcionesApiDetalle'),
    path('institucionesApi/', serialAppViews.lista_institucion, name='institucionesApi'),
    path('institucionesApi/<int:id>', serialAppViews.detalle_institucion, name='institucionesApiDetalle'),
    path('inscripciones/', inscripcionesViews.inscripciones, name='inscripciones'),
    path('instituciones/', inscripcionesViews.instituciones, name='instituciones'),

    path('agregarInstitucion/', inscripcionesViews.agregarInstitucion, name='agregarInstitucion'),
    path('actualizarInstitucion/<int:id>', inscripcionesViews.actualizarInstitucion, name='actualizarInstitucion'),
    path('eliminarInstitucion/<int:id>', inscripcionesViews.eliminarInstitucion, name='eliminarInstitucion'),

    path('agregarInscripcion/', inscripcionesViews.agregarInscripcion, name='agregarInscripcion'),
    path('actualizarInscripcion/<int:id>', inscripcionesViews.actualizarInscripcion, name='actualizarInscripcion'),
    path('eliminarInscripcion/<int:id>', inscripcionesViews.eliminarInscripcion, name='eliminarInscripcion')
]
