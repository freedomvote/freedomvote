from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
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
                        user = User.objects.create_user(username, None, password)
                        user.save()
                    except:
                        print('User creation failed')
        except:
            print('Could not parse target file')
