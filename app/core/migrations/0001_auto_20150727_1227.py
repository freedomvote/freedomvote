# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'migrate_party_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='value',
            field=models.IntegerField(verbose_name='value'),
            preserve_default=True,
        ),
    ]
