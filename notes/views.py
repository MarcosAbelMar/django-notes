from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .form import NotesForm 
from .models import Note


class NotesDelateView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/borrar_nota.html'
    success_url = '/smart/notes'
    login_url = "/login"

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/notas_form.html'
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"

    def get_success_url(self):
        obj_id = self.kwargs['pk']
        url = reverse('detalles_notas', args=[obj_id])
        return url

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/notas_form.html'
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = 'notes/lista_notas.html'
    login_url = "/login"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        notes = Note.objects.filter(user=self.request.user)

        if busqueda:
            notes = notes.filter(
                Q(titulo__icontains=busqueda) |
                Q(texto__icontains=busqueda)
            ).distinct()

        return notes

class NotesDetalleView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = "note"
    template_name = 'notes/detalles_notas.html'
    login_url = "/login"


