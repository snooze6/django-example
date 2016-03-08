# coding: utf-8

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from photos.settings import LICENSES
from photos.validators import badwords_detector

PUBLIC = 'PUB'
PRIVATE = 'PRI'
VISIBILITY = (
    (PUBLIC, 'Pública'),
    (PRIVATE, 'Privada')
)


class Photo(models.Model):
    owner = models.ForeignKey(User)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="", validators=[badwords_detector]);
    # Inicializa Django por nosotros
    created_ate = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)

    def __unicode__(self):
        return self.name


if __name__ == "__main__":
    models.Model;
