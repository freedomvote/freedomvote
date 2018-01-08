# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161216_1433'),
    ]

    operations = [
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
