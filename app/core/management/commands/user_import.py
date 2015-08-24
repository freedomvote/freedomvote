from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction
from core.models import Politician
import csv

class Command(BaseCommand):
    help = 'Imports users from a CSV file'

    def handle(self, *args, **options):
        try:
            with open(args[0], 'rb') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        username = row[0]
                        password = row[1]
                        with transaction.atomic():

                            user = User.objects.create_user(username, None, password)
                            user.save()

                            for i in range(1, 3):
                                p = Politician(user=user, first_name='Vorname', last_name='Nachname', email='vorname.nachname@example.com')
                                p.save()
                    except:
                        print('User creation failed')
        except:
            print('Could not parse target file')
