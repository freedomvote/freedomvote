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
        migrations.AlterField(
            model_name='answer',
            name='politician',
            field=models.ForeignKey(related_name='answers', verbose_name='politician', to='core.Politician'),
        ),
        migrations.AlterField(
            model_name='link',
            name='politician',
            field=models.ForeignKey(related_name='links', verbose_name='politician', to='core.Politician'),
        ),
    ]
