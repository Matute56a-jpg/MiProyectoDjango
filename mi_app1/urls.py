from django.urls import path
from . import views

urlpatterns = [
    path('crear/bodega/', views.crear_bodega, name='crear_bodega'),
    path('crear/enologo/', views.crear_enologo, name='crear_enologo'),
    path('crear/vino/', views.crear_vino, name='crear_vino'),
    path('buscar/', views.buscar_vino, name='buscar_vino'),
    path('prueba/', views.vista_de_prueba, name='vista_de_prueba'),
]