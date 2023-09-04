from django.db import models

# Create your models here.
class Cliente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.codigo, self.nombre, self.apellido, self.telefono)