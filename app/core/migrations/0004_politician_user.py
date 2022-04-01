# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0003_auto_20150521_0856"),
    ]

    operations = [
        migrations.AddField(
            model_name="politician",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=models.CASCADE,
                verbose_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
