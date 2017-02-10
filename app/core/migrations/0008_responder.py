# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161216_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'responder/', null=True, verbose_name='image', blank=True)),
                ('past_contributions', models.TextField(verbose_name='past_contributions', blank=True)),
                ('future_plans', models.TextField(verbose_name='future_plans', blank=True)),
                ('state', models.ManyToManyField(to='core.State', verbose_name='state', blank=True)),
            ],
        ),
    ]
