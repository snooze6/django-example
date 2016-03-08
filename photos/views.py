# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView

from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC


# Create your views here.

class PhotosQuerySet(object):

    def getPhotos(self, request):
        if not request.user.is_authenticated():
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos


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


class DetailView(View, PhotosQuerySet):
    def get(self, request, var):
        possible_fotos = self.getPhotos(request).filter(pk=var).select_related('owner')
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
    @method_decorator(login_required())
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

    @method_decorator(login_required())
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


class PhotosListView(View, PhotosQuerySet):
    def get(self, request):
        """
        Devuelve las fotos públicas si el usuario no está autentificado, las fotos del usuario o las públicas y si es administrador todas.
        :param request:
        :return:
        """

        context = {
            'photos': self.getPhotos(request)
        }

        return render(request, 'photos/photos_list.html', context)


class UserPhotosView(ListView):
    model = Photo
    template_name = 'photos/user_photos.html'

    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()
        return queryset.filter(owner=self.request.user)