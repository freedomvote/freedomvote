# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150401_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='description_de',
            field=models.TextField(null=True, verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='description_fr',
            field=models.TextField(null=True, verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='description_it',
            field=models.TextField(null=True, verbose_name='description', blank=True),
            preserve_default=True,
        ),
    ]
