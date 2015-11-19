# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', 'add_core_statistic_indexes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='politician',
            old_name='unique_url',
            new_name='unique_key'
        ),
    ]
