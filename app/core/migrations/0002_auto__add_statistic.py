# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Statistic'
        db.create_table(u'core_statistic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('politician', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Politician'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Category'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'core', ['Statistic'])


    def backwards(self, orm):
        # Deleting model 'Statistic'
        db.delete_table(u'core_statistic')


    models = {
        u'core.answer': {
            'Meta': {'object_name': 'Answer'},
            'agreement_level': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Politician']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Question']"})
        },
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
            'future_plans': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_member_of_parliament': ('django.db.models.fields.BooleanField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Party']", 'null': 'True', 'blank': 'True'}),
            'party_other': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'past_contributions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.State']", 'null': 'True', 'blank': 'True'}),
            'unique_url': ('django.db.models.fields.CharField', [], {'default': "'Pvm8-ZU3N1cTJ4xIAhY4'", 'max_length': '20'})
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
        },
        u'core.statistic': {
            'Meta': {'object_name': 'Statistic'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Politician']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['core']