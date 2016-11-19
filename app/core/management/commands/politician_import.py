from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from core.models import Politician, State, Party
from django.db import transaction
import csv

class Command(BaseCommand):
    help = 'Imports politician from a [csv_file]. Each row of the csv file is expected to be structured like: first_name, last_name, email, state, party, user, member_of_parliament. The rows that were succesfully imported, have their resulted import written into \'/tmp/export.csv\'. This export file is of the structure: first_name, last_name, email, state.name, party.shortname, user.username, politician.unique_url.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='file to import')

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            rows = []

            with open(options['csv_file'], 'rb') as csvfile:
                reader = csv.reader(csvfile)
                count = 0
                for row in reader:
                    row = [col.decode('utf-8') for col in row]
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
                    except Exception as e:
                        print('Politician creation on line %d failed: %s' % (count, e))
            with open('/tmp/export.csv', 'wb') as csvfile:
                writer = csv.writer(csvfile)
                for row in rows:
                    writer.writerow([c.encode('utf8') for c in row])

                print('Export file is located in /tmp/export.csv')

        except Exception as e:
            print(str(e))
            print('Could not parse target file')
# vim: set sw=4:ts=4:et:
