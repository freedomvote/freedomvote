# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20161216_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unique_key', models.CharField(default=core.models.generate_url, max_length=20, verbose_name='unique_key')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='politician',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]
