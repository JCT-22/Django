from django.db import models
from django.utils.html import format_html

from .choices import sexos


class Docente(models.Model):
     #creamos una nueva tabla de base de datos 
     #llamada docente y realizamos particiones "apellidos", "nombres",sexo. etc
    Apellido_Paterno = models.CharField(max_length=20,verbose_name="Apellido Paterno")
    Apellido_Materno = models.CharField(max_length=20,verbose_name="Apellido Materno")
    nombres = models.CharField(max_length=20,verbose_name="Nombres")
    fecha_nacimiento = models.DateField (verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=1, choices=sexos,default='F')

    def nombre_completo(self):
         return"{}{},{}".format(self.Apellido_Paterno, self.Apellido_Materno, self.nombres)
    def __str__(self):
         return self.nombre_completo()
    
    class Meta: # class meta es para configurar la base de datos
         verbose_name = 'Docente'
         verbose_name_plural ='Docentes'
         db_table = 'Docente'
         ordering =['Apellido_Paterno','-Apellido_Materno']
# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length =38)#indicamos que la variable nobre va tener un maximo de 30 caracteres
    #creamos un campo de baso de dato llamado creditos entero positivo de pequeño rango
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(Docente,null = True,blank =True,on_delete =models.CASCADE)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    
    def coloreado(self):
        if  self.creditos > 30: 
              return format_html('<span style = "color: blue;">{0}</span>'.format(self.nombre))
        else:
             return format_html('<span style ="color: red;">{0}</span>'.format(self.nombre))
    