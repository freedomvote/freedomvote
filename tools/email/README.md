# Email generator

This Python script was used in the original Swiss Freedomvote campaign to generate emails for the parties.

## Steps involved

1. Create accounts for the parties in the Freedomvote software, which can be done using the import features in `manage.py`.
2. Gather contact details of the parties and create a `party_accounts.csv` file in a structure similar to the included `party_accounts_example.csv` file.
3. Customize the email template `party_account_template_de.eml`. The filename is hardcoded inside the script. The FULL_CAPS keywors are placeholders for the script.
4. Run the Python script to generate emails for each party account: `python gen_mails.py`

