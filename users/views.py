# coding=utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import logout as lojout, authenticate, login as lojin


# Create your views here.


def login(request):
    error_messages=[]
    if request.method == 'POST':
        # # Esto peta cuando cambiamos el name de l formulario
        # username = request.POST['usr']
        # password = request.POST['pwd']
        username = request.POST.get('usr')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append("Nombre de usuario o contraseña incorrectos")
        else:
            if user.is_active:
                lojin(request, user)
                return redirect('photos_home')
            else:
                error_messages.append("El usuario no está activo")
    context = {
        'errors': error_messages
    }
    return render(request, 'users/login.html', context)


def logout(request):
    if request.user.is_authenticated():
        lojout(request)
    return redirect('photos_home')