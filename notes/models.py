from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
