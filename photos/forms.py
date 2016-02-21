from django import forms

from photos.models import Photo


class PhotoForm(forms.ModelForm):
    """
    No funciono
    """

    class Meta:
        model = Photo
        exclude = []