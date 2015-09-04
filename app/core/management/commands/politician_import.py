from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from core.models import Politician
import csv

class Command(BaseCommand):
    help = 'Imports politician from a CSV file'

    def handle(self, *args, **options):
        try:
            with open(args[0], 'rb') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    try:
                        user       = User.objects.get(username=row[0])
                        first_name = row[1]
                        last_name  = row[2]
                        email      = row[3]

                        p = Politician(
                            user=user,
                            first_name=first_name,
                            last_name=last_name,
                            email=email
                        )
                        p.save()
                    except:
                        print('Politician creation failed')
        except:
            print('Could not parse target file')
