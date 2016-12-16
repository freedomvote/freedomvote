from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import json

class Command(BaseCommand):
    help = 'Imports users from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', help='JSON file to import')

    def handle(self, *args, **options):
        try:
            with open(options['json_file']) as f:
                data = json.load(f)

                for row in data:
                    try:
                        user = User.objects.create_user(
                            row.get('username'),
                            None,
                            row.get('password')
                        )

                        user.save()
                    except:
                        print('User creation failed')

        except:
            print(str(e))

# vim: set sw=4:ts=4:et:
