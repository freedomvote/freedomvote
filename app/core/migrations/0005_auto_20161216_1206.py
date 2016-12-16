# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161214_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='state',
            field=models.ManyToManyField(to='core.State', verbose_name='state', blank=True),
        ),
    ]
