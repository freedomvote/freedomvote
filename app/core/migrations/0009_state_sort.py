# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_auto_20180110_1256"),
    ]

    operations = [
        migrations.AddField(
            model_name="state",
            name="sort",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
