# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20160220_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, default='', null=True, validators=[photos.validators.badwords_detector]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(choices=[(b'BSD', b'BSD-Open'), (b'RIG', b'CopyRight'), (b'LEF', b'CopyLeft'), (b'CC', b'Creative Commons')], max_length=3),
        ),
    ]