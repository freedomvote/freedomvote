from south.db import db
from south.v2 import SchemaMigration

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.execute('''
            CREATE OR REPLACE FUNCTION core_statistic_compare(value integer, expectation integer) RETURNS double precision
                LANGUAGE plpgsql IMMUTABLE
                AS $$
            DECLARE
                accordance double precision;
            BEGIN
                RETURN (10 - ( abs(value - expectation) / 10));
            END;
            $$;
        ''')
        print('Created function core_statistic_compare...')
        for x in range(0, 101):
            db.execute('CREATE INDEX core_statistic_value_%d ON core_statistic (core_statistic_compare(value::integer, %d))' % (x,x))

            print('Index core_statistic_value_%d created...' % x)

        db.execute('TRUNCATE TABLE core_statistic')
        print('Truncated table core_statistic...')

    def backwards(self, orm):
        pass
