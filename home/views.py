from django.shortcuts import render
from datetime import date
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


class CustomUserCreationForm(UserCreationForm):
    error_messages = {}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.error_messages['password_mismatch'] = 'Las contraseñas no coinciden.'

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('lista_notas')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
   
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    fecha_actual = date.today()
    extra_context =  {'today': fecha_actual}

    
