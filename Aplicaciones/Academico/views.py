from django.shortcuts import render
#from django.http import HttpResponse
from .models import Curso
# Create your views here.

# 192.168.100.67
# 255.255.255.0

def home(request):
    #cursosListados = Curso.objects.all()
    #cursosListados = Curso.objects.all()[:5] #muestra los 5 primeros elementos
    #cursosListados = Curso.objects.all()[3:7]  #  ahora muestra solo los del 3 al 7
    #cursosListados = Curso.objects.all().order_by('nombre') #ordena la tabla alfabeticamente 
    #cursosListados = Curso.objects.all().order_by('-nombre') #ahora de manera inversa
    #cursosListados = Curso.objects.all().order_by('nombre','creditos') # utilizamos un segundo criterio 'creditos'
    #cursosListados = Curso.objects.filter(nombre = 'Calculo II')  #ahora filtramos de la tabla solo el elemento historia
    #cursosListados = Curso.objects.filter(creditos__gte=4) # ahora  filtramos solo los creditos mayores a 4
    #cursosListados = Curso.objects.filter(nombre__startswith='C')
    cursosListados = Curso.objects.filter(nombre__contains='m')
    return render(request,"gestionCursos.html",{"cursos":cursosListados})

