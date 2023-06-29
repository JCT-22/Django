from django.contrib import admin
from .models import Curso ,Docente
# Registra tus modelos aqui

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ["id","coloreado","creditos"] #modificacion  de los elememtos de la tabla admin :)
    #ordering =("nombre",) #para ordenar por nombre la lista 
    #search_fields = ("nombre","creditos") #agrega una barra de busqueda amigable
    #list_editable = ["nombre","creditos"] #ahora podemos editar el nombre en la misma tabla 
    
    fieldsets=(
        (None,{'fields':('nombre',) #aqui indicamos que solo se pueda modificar nombre de los curso
        }),
        ('Advance options',{
                    'classes':('collapse', 'wide', 'extrapretty'),
                    'fields':('creditos',) #aquie decimos los creditos son opciones avanzadas 
        })
    )

    def datos(self,obj):
        return obj.nombre.upper()
    
    datos.short_description = 'CURSO (MAYÙS)' # para cambiar el titulo de las columna 
    datos.empty_value_display = '???' # cuando tenga un valor vacio POn "???"
    datos.admin_order_field = 'nombre' # indicamos  que el campo de ordenamiento el por el nombre 

#admin.site.unregister(Curso)
#admin.site.register(Curso,CursoAdmin)

#admin.site.register(Docente)

