# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_auto_20150727_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ['name'], 'verbose_name': 'party', 'verbose_name_plural': 'parties'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['category__name'], 'verbose_name': 'question', 'verbose_name_plural': 'questions'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['name'], 'verbose_name': 'state', 'verbose_name_plural': 'states'},
        ),
        migrations.AlterField(
            model_name='politician',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='first_name',
            field=models.CharField(max_length=100, null=True, verbose_name='first_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='politician',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='last_name', blank=True),
            preserve_default=True,
        ),
    ]
