# coding=utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import logout as lojout, authenticate, login as lojin

# Create your views here.
from django.views.generic import View

from users.forms import LoginForm


class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        # # # Esto peta cuando cambiamos el name de l formulario
        # # username = request.POST['usr']
        # # password = request.POST['pwd']
        # username = request.POST.get('usr')
        # password = request.POST.get('pwd')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append("Nombre de usuario o contraseña incorrectos")
            else:
                if user.is_active:
                    lojin(request, user)
                    return redirect(request.GET.get("next", 'photos_home'))
                else:
                    error_messages.append("El usuario no está activo")

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            lojout(request)
        return redirect('photos_home')
