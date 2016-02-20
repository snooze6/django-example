from django.shortcuts import render, redirect
from django.contrib.auth import logout as lojout

# Create your views here.


def login(request):
    pass


def logout(request):
    if request.user.is_authenticated():
        lojout(request)
    return redirect('photos_home')