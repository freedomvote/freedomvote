# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'State'
        db.create_table(u'core_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_it', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['State'])

        # Adding model 'Party'
        db.create_table(u'core_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_it', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('shortname', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('shortname_de', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('shortname_fr', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('shortname_it', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Party'])

        # Adding model 'Category'
        db.create_table(u'core_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_it', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Category'])

        # Adding model 'Politician'
        db.create_table(u'core_politician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('is_member_of_parliament', self.gf('django.db.models.fields.BooleanField')()),
            ('past_contributions', self.gf('django.db.models.fields.TextField')(null=True)),
            ('future_plans', self.gf('django.db.models.fields.TextField')(null=True)),
            ('unique_url', self.gf('django.db.models.fields.CharField')(default='w1cCW8w__g5cDGs0nDom', max_length=20)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.State'])),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Party'], null=True)),
            ('party_other', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'core', ['Politician'])

        # Adding model 'Question'
        db.create_table(u'core_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('preferred_answer', self.gf('django.db.models.fields.IntegerField')()),
            ('question_number', self.gf('django.db.models.fields.IntegerField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Category'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_it', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Question'])


    def backwards(self, orm):
        # Deleting model 'State'
        db.delete_table(u'core_state')

        # Deleting model 'Party'
        db.delete_table(u'core_party')

        # Deleting model 'Category'
        db.delete_table(u'core_category')

        # Deleting model 'Politician'
        db.delete_table(u'core_politician')

        # Deleting model 'Question'
        db.delete_table(u'core_question')


    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'core.party': {
            'Meta': {'object_name': 'Party'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'shortname_de': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'shortname_fr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'shortname_it': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'core.politician': {
            'Meta': {'object_name': 'Politician'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'future_plans': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'is_member_of_parliament': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Party']", 'null': 'True'}),
            'party_other': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'past_contributions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.State']"}),
            'unique_url': ('django.db.models.fields.CharField', [], {'default': "'tKqQs7enwEcm6vhGRPgJ'", 'max_length': '20'})
        },
        u'core.question': {
            'Meta': {'object_name': 'Question'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preferred_answer': ('django.db.models.fields.IntegerField', [], {}),
            'question_number': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']