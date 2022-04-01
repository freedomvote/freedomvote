#!/usr/bin/python3
# -*- coding: utf8

import re
import csv
import codecs

SENDER = "freedomvote@freedomvote.ch"

reader = csv.reader(codecs.open("party_accounts.csv", encoding="UTF-8"))

template = codecs.open("party_account_template_de.eml", encoding="UTF-8").read()

seen_parties = set()

for row in reader:
    if row[0] == "State":
        # Header Row
        continue

    # State,Party,Login,Password,Address 1,Address 2,Street,Post office box,City,Phone,Fax,Email,Note
    # 0     1     2     3        4         5         6      7               8    9     10  11    12
    state = row[0]
    party = row[1]
    login = row[2]
    password = row[3]
    recipient = row[11]

    if recipient == "":
        print("Warning: %s %s has no email address!" % (party, state))

    # Check for duplicates
    dup_key = ("%s-%s" % (party, state)).lower()
    if (dup_key) in seen_parties:
        # Duplicate
        print("Warning: duplicate entry, skipping: %s %s" % (party, state))
        continue
    seen_parties.add(dup_key)

    # Genereate mail text from template
    mail = (
        template.replace("RECIPIENT", recipient)
        .replace("FROM", SENDER)
        .replace("LINK", "http://freedomvote.ch/party/%s" % login)
        .replace("PASSWORD", password)
    )

    # Write result
    outfile = "generated_freedomvote_mail_%s_%s.eml" % (party, state)

    outfile = re.sub(r"[^\.\w0-9]", "_", outfile).lower()

    with codecs.open(outfile, "w", encoding="UTF-8") as fh:
        fh.write(mail)
