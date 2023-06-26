from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length =38)#indicamos que la variable nobre va tener un maximo de 30 caracteres
    #creamos un campo de baso de dato llamado creditos entero positivo de pequeño rango
    creditos = models.PositiveSmallIntegerField()
