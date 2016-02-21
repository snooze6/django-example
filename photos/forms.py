# coding=utf-8
from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):
    """
    No funciono
    """

    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """
        Valida la descripción
        :return:
        """
        cleared_data = super(PhotoForm, self).clean()
        description = cleared_data.get('description', '')

        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError(u'La palabra {0} no está admitida'.format(badword))

        return cleared_data
