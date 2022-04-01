# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "agreement_level",
                    models.IntegerField(verbose_name="agreement_level"),
                ),
                ("note", models.TextField(verbose_name="note")),
            ],
            options={
                "verbose_name": "answer",
                "verbose_name_plural": "answers",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                (
                    "name_de",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_fr",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_it",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("url", models.URLField(verbose_name="url")),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="LinkType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("icon", models.ImageField(upload_to=b"icons/", verbose_name="icon")),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                (
                    "name_de",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_fr",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_it",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Party",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                (
                    "name_de",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_fr",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_it",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "shortname",
                    models.CharField(max_length=10, verbose_name="shortname"),
                ),
                (
                    "shortname_de",
                    models.CharField(
                        max_length=10, null=True, verbose_name="shortname"
                    ),
                ),
                (
                    "shortname_fr",
                    models.CharField(
                        max_length=10, null=True, verbose_name="shortname"
                    ),
                ),
                (
                    "shortname_it",
                    models.CharField(
                        max_length=10, null=True, verbose_name="shortname"
                    ),
                ),
            ],
            options={
                "verbose_name": "party",
                "verbose_name_plural": "parties",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Politician",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="first_name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="last_name"),
                ),
                ("email", models.EmailField(max_length=75, verbose_name="email")),
                (
                    "image",
                    models.ImageField(
                        upload_to=b"politicians/",
                        null=True,
                        verbose_name="image",
                        blank=True,
                    ),
                ),
                (
                    "is_member_of_parliament",
                    models.BooleanField(
                        default=False, verbose_name="is_member_of_parliament"
                    ),
                ),
                (
                    "past_contributions",
                    models.TextField(verbose_name="past_contributions", blank=True),
                ),
                (
                    "future_plans",
                    models.TextField(verbose_name="future_plans", blank=True),
                ),
                (
                    "unique_url",
                    models.CharField(
                        default=core.models.generate_url,
                        max_length=20,
                        verbose_name="unique_url",
                    ),
                ),
                (
                    "party_other",
                    models.CharField(
                        max_length=50, null=True, verbose_name="party_other", blank=True
                    ),
                ),
                (
                    "party",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        verbose_name="party",
                        blank=True,
                        to="core.Party",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "politician",
                "verbose_name_plural": "politicians",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "preferred_answer",
                    models.IntegerField(verbose_name="preferred_answer"),
                ),
                (
                    "question_number",
                    models.IntegerField(verbose_name="question_number"),
                ),
                ("text", models.TextField(verbose_name="text")),
                ("text_de", models.TextField(null=True, verbose_name="text")),
                ("text_fr", models.TextField(null=True, verbose_name="text")),
                ("text_it", models.TextField(null=True, verbose_name="text")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        verbose_name="category",
                        to="core.Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "question",
                "verbose_name_plural": "questions",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                (
                    "name_de",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_fr",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
                (
                    "name_it",
                    models.CharField(max_length=50, null=True, verbose_name="name"),
                ),
            ],
            options={
                "verbose_name": "state",
                "verbose_name_plural": "states",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Statistic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("value", models.FloatField(verbose_name="value")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        verbose_name="category",
                        to="core.Category",
                    ),
                ),
                (
                    "politician",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        verbose_name="politician",
                        to="core.Politician",
                    ),
                ),
            ],
            options={
                "verbose_name": "statistic",
                "verbose_name_plural": "statistics",
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name="politician",
            name="state",
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                verbose_name="state",
                blank=True,
                to="core.State",
                null=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="link",
            name="politician",
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                verbose_name="politician",
                to="core.Politician",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="link",
            name="type",
            field=models.ForeignKey(
                on_delete=models.CASCADE, verbose_name="type", to="core.LinkType"
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="answer",
            name="politician",
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                verbose_name="politician",
                to="core.Politician",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=models.CASCADE, verbose_name="question", to="core.Question"
            ),
            preserve_default=True,
        ),
    ]
