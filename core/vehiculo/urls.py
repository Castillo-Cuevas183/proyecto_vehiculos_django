from django.urls import path
from .views import agregar_vehiculo, listar_vehiculos
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal de la aplicación
    path('vehiculo/add/', agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/listar/', listar_vehiculos, name='listar_vehiculos'),
    ]
