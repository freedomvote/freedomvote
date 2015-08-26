from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction
from core.models import Politician
import csv

class Command(BaseCommand):
    help = 'Generates x politicians for a user'

    def handle(self, *args, **options):
        try:
            count = int(args[0])
        except:
            count = 1

        try:
            with transaction.atomic():
                for user in User.objects.all():
                    for i in range(0, count):
                        p = Politician(
                            user=user,
                            first_name='Vorname',
                            last_name='Nachname',
                            email='vorname.nachname@example.com'
                        )
                        p.save()
        except:
            print('Transaction failed')

        try:
            with open('export.csv', 'wb') as csvfile:
                writer = csv.writer(csvfile)

                for user in User.objects.all():
                    writer.writerow(
                        [ user.username ] +
                        [ x.unique_url for x in Politician.objects.filter(user=user)  ]
                    )

        except:
            print('Export failed')
