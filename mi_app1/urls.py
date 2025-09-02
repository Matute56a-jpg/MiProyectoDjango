from django.urls import path
from . import views
import os

print("CARGADO mi_app1/urls.py DESDE:", os.path.abspath(__file__))

urlpatterns = [
    path('crear/bodega/', views.crear_bodega, name='crear_bodega'),
    path('crear/enologo/', views.crear_enologo, name='crear_enologo'),
    path('crear/vino/', views.crear_vino, name='crear_vino'),
    path('buscar/', views.buscar_vino, name='buscar_vino'),
    path('vinos/', views.lista_vinos, name='lista_vinos'),
    path('prueba/', views.prueba, name='vista_de_prueba'),
]