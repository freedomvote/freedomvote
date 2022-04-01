# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_party_color"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="party",
            name="color",
        ),
        migrations.AddField(
            model_name="party",
            name="background_color",
            field=colorfield.fields.ColorField(
                default=b"#3F51B5", max_length=10, verbose_name="background_color"
            ),
        ),
        migrations.AddField(
            model_name="party",
            name="font_color",
            field=colorfield.fields.ColorField(
                default=b"#FFFFFF", max_length=10, verbose_name="font_color"
            ),
        ),
    ]
