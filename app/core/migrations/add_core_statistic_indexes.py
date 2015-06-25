from django.db import migrations

def add_indexes(apps, schema_editor):
    for x in range(0, 101):
        schema_editor.execute('CREATE INDEX core_statistic_value_%d ON core_statistic (core_statistic_compare(value::integer, %d))' % (x,x))

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial')
    ]

    operations = [
    migrations.RunSQL('''
        CREATE OR REPLACE FUNCTION core_statistic_compare(value integer, expectation integer) RETURNS double precision
            LANGUAGE plpgsql IMMUTABLE
            AS $$
        DECLARE
            accordance double precision;
        BEGIN
            RETURN (10 - ( abs(value - expectation) / 10));
        END;
        $$;
    '''),
    migrations.RunPython(add_indexes),
    migrations.RunSQL('TRUNCATE TABLE core_statistic')
    ]
