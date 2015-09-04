from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from core.models import Politician, State, Party
import csv

class Command(BaseCommand):
    help = 'Imports politician from a CSV file'

    def handle(self, *args, **options):
        try:
            rows = []

            with open(args[0], 'rt') as csvfile:
                reader = csv.reader(csvfile)
                count = 0
                for row in reader:
                    count += 1
                    try:
                        first_name = row[0]
                        last_name  = row[1]
                        email      = row[2]
                        state      = State.objects.get(name=row[3])
                        party      = Party.objects.get(shortname=row[4])
                        user       = User.objects.get(username=row[5])
                        member     = bool(row[6])

                        p = Politician(
                            user=user,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            state=state,
                            party=party,
                            is_member_of_parliament=member
                        )
                        p.save()

                        rows.append([first_name, last_name, email, state.name, party.shortname, user.username, p.unique_url])
                    except:
                        print('Politician creation on line %d failed' % count)
            with open('/tmp/export.csv', 'wb') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows)

                print('Export file is located in /tmp/export.csv')

        except:
            print('Could not parse target file')
