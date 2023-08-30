from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="lista_notas"),
    path('detail/<int:pk>', views.NotesDetalleView.as_view(), name="detalles_notas"),
    path('detail/<int:pk>/edit', views.NotesUpdateView.as_view(), name="editar_nota"),
    path('detail/<int:pk>/delete', views.NotesDelateView.as_view(), name="eliminar_nota"),
    path('notes/new', views.NotesCreateView.as_view(), name="nueva_nota"),
]