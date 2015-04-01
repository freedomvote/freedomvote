# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'rename_core_politician_unique_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'link', 'verbose_name_plural': 'links'},
        ),
        migrations.AlterModelOptions(
            name='linktype',
            options={'verbose_name': 'link_type', 'verbose_name_plural': 'link_types'},
        ),
        migrations.AlterField(
            model_name='politician',
            name='unique_key',
            field=models.CharField(default=core.models.generate_url, max_length=20, verbose_name='unique_key'),
            preserve_default=True,
        ),
    ]
