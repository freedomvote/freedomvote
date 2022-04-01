# -*- coding: utf-8 -*-
from django.db import migrations
from django.contrib.auth.models import User
import csv
import re
import string
from random import *


def generate_password(length=12):
    characters = string.ascii_letters + "#@+-&%()?!*" + string.digits
    return "".join(choice(characters) for x in range(length))


def add_user_for_parties(apps, schema_editor):
    Party = apps.get_model("core", "Party")

    parties = Party.objects.all()

    for party in parties:
        username_raw = re.sub(
            "ö",
            "oe",
            re.sub(
                "ü", "ue", re.sub("ä", "ae", party.shortname.encode("utf8").lower())
            ),
        )
        username = re.sub("[^a-zA-Z]", "", username_raw)

        password = generate_password()

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.save()
        else:
            continue


class Migration(migrations.Migration):
    dependencies = [("core", "0004_politician_user")]

    operations = [migrations.RunPython(add_user_for_parties)]
