# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_auto_20160106_0925"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="link",
            name="type",
        ),
        migrations.AddField(
            model_name="category",
            name="name_en",
            field=models.CharField(max_length=50, null=True, verbose_name="name"),
        ),
        migrations.AddField(
            model_name="category",
            name="name_nl",
            field=models.CharField(max_length=50, null=True, verbose_name="name"),
        ),
        migrations.AddField(
            model_name="party",
            name="name_en",
            field=models.CharField(max_length=50, null=True, verbose_name="name"),
        ),
        migrations.AddField(
            model_name="party",
            name="name_nl",
            field=models.CharField(max_length=50, null=True, verbose_name="name"),
        ),
        migrations.AddField(
            model_name="party",
            name="shortname_en",
            field=models.CharField(max_length=10, null=True, verbose_name="shortname"),
        ),
        migrations.AddField(
            model_name="party",
            name="shortname_nl",
            field=models.CharField(max_length=10, null=True, verbose_name="shortname"),
        ),
        migrations.AddField(
            model_name="question",
            name="description_en",
            field=models.TextField(null=True, verbose_name="description", blank=True),
        ),
        migrations.AddField(
            model_name="question",
            name="description_nl",
            field=models.TextField(null=True, verbose_name="description", blank=True),
        ),
        migrations.AddField(
            model_name="question",
            name="text_en",
            field=models.TextField(null=True, verbose_name="text"),
        ),
        migrations.AddField(
            model_name="question",
            name="text_nl",
            field=models.TextField(null=True, verbose_name="text"),
        ),
        migrations.AddField(
            model_name="state",
            name="name_en",
            field=models.CharField(max_length=50, null=True, verbose_name="name"),
        ),
        migrations.AddField(
            model_name="state",
            name="name_nl",
            field=models.CharField(max_length=50, null=True, verbose_name="name"),
        ),
        migrations.RemoveField(
            model_name="politician",
            name="state",
        ),
        migrations.AddField(
            model_name="politician",
            name="state",
            field=models.ManyToManyField(
                to="core.State", null=True, verbose_name="state", blank=True
            ),
        ),
        migrations.DeleteModel(
            name="LinkType",
        ),
    ]
