# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161216_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='color',
            field=colorfield.fields.ColorField(default=b'#FF0000', max_length=10, verbose_name='color'),
        ),
    ]
