# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150824_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email', blank=True),
        ),
    ]
