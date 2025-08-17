from django import forms
from .models import Bodega, Enologo, Vino

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['nombre', 'ubicacion', 'año_fundacion']

class EnologoForm(forms.ModelForm):
    class Meta:
        model = Enologo
        fields = ['nombre', 'experiencia', 'especialidad']

class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = ['nombre', 'tipo', 'año_cosecha', 'bodega', 'enologo']