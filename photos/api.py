# coding=utf-8
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotosQuerySet


class PhotoViewSet(PhotosQuerySet, ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.getPhotosQuerySet(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la foto al usuario autenticado
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)


# class PhotoListAPI(ListCreateAPIView, PhotosQuerySet):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoListSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_serializer_class(self):
#         return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer
#
#     def get_queryset(self):
#         return self.getPhotosQuerySet(self.request)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class PhotoDetailAPI(RetrieveUpdateDestroyAPIView, PhotosQuerySet):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         return self.getPhotosQuerySet(self.request)
