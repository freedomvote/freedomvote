# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161216_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='note_de',
            field=models.TextField(null=True, verbose_name='note'),
        ),
        migrations.AddField(
            model_name='answer',
            name='note_en',
            field=models.TextField(null=True, verbose_name='note'),
        ),
        migrations.AddField(
            model_name='answer',
            name='note_fr',
            field=models.TextField(null=True, verbose_name='note'),
        ),
        migrations.AddField(
            model_name='answer',
            name='note_it',
            field=models.TextField(null=True, verbose_name='note'),
        ),
        migrations.AddField(
            model_name='answer',
            name='note_nl',
            field=models.TextField(null=True, verbose_name='note'),
        ),
    ]
