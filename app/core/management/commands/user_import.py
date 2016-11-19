from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import csv

class Command(BaseCommand):
    help = "Imports users from a [csv_file]. Each row in the CSV file should contain: username, password."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='file to import')

    def handle(self, *args, **options):
        try:
            with open(options['csv_file'], 'rb') as csvfile:
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
