from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


# Create your views here.


def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_ate')

    # html = '<ul>'
    # for photo in photos:
    #     html += '<li>' + photo.name + '</li>'
    # html += '</ul>'
    # return HttpResponse(html)

    context = {
        'photos_list': photos[:5]
    }

    return render(request, 'photos/home.html', context)

    # if len(request.GET)!=0:
    #     a = "<h1>Hola</h1>"
    #     for i in request.GET:
    #         a+="<p>"+i+" - "+request.GET[i]+"</p>"
    #     return HttpResponse(a)
    # else:
    #     return HttpResponse("<h1>Hola</h1>"+"<p>Cero argumentos</p>")


def detail(request, var):
    possible_fotos = Photo.objects.filter(pk=var)
    foto = possible_fotos[0] if len(possible_fotos) == 1 else None
    if foto is not None:
        # load detail
        context = {
            'photo': foto
        }
        return render(request, 'photos/detail.html', context);
    else:
        return HttpResponseNotFound("No existe la foto")

def new_photo(request):
    """
    Muestra un formulario
    :param request:
    :return:
    """

    if request.method=='GET':
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save() #Guarda el objeto y me lo devuelve
    context = {
        'form': form
    }
    return render(request, 'photos/new_photo.html', context)
