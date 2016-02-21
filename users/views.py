# coding=utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import logout as lojout, authenticate, login as lojin


# Create your views here.
from users.forms import LoginForm


def login(request):
    error_messages=[]
    if request.method == 'POST':
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
    else:
        form = LoginForm()
    context = {
        'errors': error_messages,
        'login_form': form
    }
    return render(request, 'users/login.html', context)


def logout(request):
    if request.user.is_authenticated():
        lojout(request)
    return redirect('photos_home')