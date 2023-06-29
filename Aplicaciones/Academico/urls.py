from django.urls import path
from Aplicaciones.Academico.views import CursoListView

urlpatterns = [
    path('',CursoListView.as_view(),name="Gestion_cursos")
]