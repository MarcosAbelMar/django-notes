from django import forms
from .models import Note

class NotesForm(forms.ModelForm):
    class Meta:
        model = Note 
        fields =('titulo', 'texto')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control my-2' }), 
            'texto': forms.Textarea(attrs={'class':'form-control' })
        }

        

