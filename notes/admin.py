from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'creado')

admin.site.register(models.Note, NotesAdmin)
