from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)
    año_fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre

class Enologo(models.Model):
    nombre = models.CharField(max_length=100)
    experiencia = models.IntegerField(help_text="Años de experiencia")
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[("Tinto", "Tinto"), ("Blanco", "Blanco"), ("Rosado", "Rosado")])
    año_cosecha = models.IntegerField()
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    enologo = models.ForeignKey(Enologo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.año_cosecha})"