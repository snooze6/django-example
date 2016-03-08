# coding=utf-8
from rest_framework.exceptions import ValidationError

from photos.settings import BADWORDS


def badwords_detector(value):
        """
        Valida 'value'
        :return: Boolean
        """

        for badword in BADWORDS:
            if badword.lower() in value.lower():
                raise ValidationError(u'La palabra {0} no está admitida'.format(badword))

        return True