from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
#from django.http import HttpResponse
from .models import Curso
# Create your views here.

# 192.168.100.67
# 255.255.255.0

def home(request):
    cursosListados = Curso.objects.all()
    #cursosListados = Curso.objects.all()[:5] #muestra los 5 primeros elementos
    #cursosListados = Curso.objects.all()[3:7]  #  ahora muestra solo los del 3 al 7
    #cursosListados = Curso.objects.all().order_by('nombre') #ordena la tabla alfabeticamente 
    #cursosListados = Curso.objects.all().order_by('-nombre') #ahora de manera inversa
    #cursosListados = Curso.objects.all().order_by('nombre','creditos') # utilizamos un segundo criterio 'creditos'
    #cursosListados = Curso.objects.filter(nombre = 'Calculo II')  #ahora filtramos de la tabla solo el elemento historia
    #cursosListados = Curso.objects.filter(creditos__gte=4) # ahora  filtramos solo los creditos mayores a 4
    #cursosListados = Curso.objects.filter(nombre__startswith='C')
    #cursosListados = Curso.objects.filter(nombre__contains='m') #filtra solo los que contengan la letra m
    data = {'titulo':'Gestion de mis cursos','cursos':cursosListados}
    #return render(request,"gestionCursos.html",{"cursos":cursosListados})
    return render(request, 'gestionCursos.html',data)
#user name = JCT-22
#password = 12345678

class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'gestion de cursos'
        #print(context)
        return context
