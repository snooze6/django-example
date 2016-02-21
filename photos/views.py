# coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


# Create your views here.


class HomeView(View):
    def get(self, request):
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


class DetailView(View):
    def get(self, request, var):
        possible_fotos = Photo.objects.filter(pk=var).select_related('owner')
        foto = possible_fotos[0] if len(possible_fotos) == 1 else None
        if foto is not None:
            # load detail
            context = {
                'photo': foto
            }
            return render(request, 'photos/detail.html', context);
        else:
            return HttpResponseNotFound("No existe la foto")


class CreateView(View):
    @login_required()
    def get(self, request):
        """
        Muestra un formulario
        :param request:
        :return:
        """

        form = PhotoForm()
        context = {
            'form': form,
        }
        return render(request, 'photos/new_photo.html', context)

    @login_required()
    def post(self, request):
        """
        Muestra un formulario
        :param request:
        :return:
        """
        sucess_message = []

        # Es esto seguro? -> Que pasa si meto owner con POST
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user
        form = PhotoForm(request.POST, instance=photo_with_owner)

        if form.is_valid():
            photo = form.save()  # Guarda el objeto y me lo devuelve
            sucess_message = 'Guardado con éxito '
            sucess_message += '<a href=\"{0}\">'.format(reverse('photos_detail', args=[photo.pk]))
            sucess_message += 'Ver foto'
            sucess_message += '</a>'
        form = PhotoForm()

        context = {
            'form': form,
            'sucess_message': sucess_message
        }
        return render(request, 'photos/new_photo.html', context)
