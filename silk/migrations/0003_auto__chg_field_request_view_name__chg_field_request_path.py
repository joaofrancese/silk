# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        if 'mysql' in settings.DATABASES['default']['ENGINE']:
            # For MySQL, these fields are created with a 255 lenght since the first migration.
            return

        if 'sqlserver' in settings.DATABASES['default']['ENGINE']:
            # SQL Server requires the indices to be dropped and re-created; alter column cannot be used in an indexed column.
            db.delete_index(u'silk_request', ['view_name'])
            db.delete_index(u'silk_request', ['path'])

        # Changing field 'Request.view_name'
        db.alter_column(u'silk_request', 'view_name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Request.path'
        db.alter_column(u'silk_request', 'path', self.gf('django.db.models.fields.CharField')(max_length=255))

        if 'sqlserver' in settings.DATABASES['default']['ENGINE']:
            db.create_index(u'silk_request', ['view_name'])
            db.create_index(u'silk_request', ['path'])

    def backwards(self, orm):
        if 'mysql' in settings.DATABASES['default']['ENGINE']:
            # For MySQL, these fields are created with a 255 lenght since the first migration.
            return

        if 'sqlserver' in settings.DATABASES['default']['ENGINE']:
            # SQL Server requires the indices to be dropped and re-created; alter column cannot be used in an indexed column.
            db.delete_index(u'silk_request', ['view_name'])
            db.delete_index(u'silk_request', ['path'])

        # Changing field 'Request.view_name'
        db.alter_column(u'silk_request', 'view_name', self.gf('django.db.models.fields.CharField')(max_length=300))

        # Changing field 'Request.path'
        db.alter_column(u'silk_request', 'path', self.gf('django.db.models.fields.CharField')(max_length=300))

        if 'sqlserver' in settings.DATABASES['default']['ENGINE']:
            db.create_index(u'silk_request', ['view_name'])
            db.create_index(u'silk_request', ['path'])

    models = {
        u'silk.profile': {
            'Meta': {'object_name': 'Profile'},
            'dynamic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_line_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'exception_raised': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'file_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'func_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'queries': ('django.db.models.fields.related.ManyToManyField', [], {'db_index': 'True', 'related_name': "'profiles'", 'symmetrical': 'False', 'to': u"orm['silk.SQLQuery']"}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['silk.Request']", 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'time_taken': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'silk.request': {
            'Meta': {'object_name': 'Request'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'encoded_headers': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_num_queries': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meta_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'meta_time_spent_queries': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'num_sql_queries': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'pyprofile': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'query_params': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'raw_body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'time_taken': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'view_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'db_index': 'True', 'blank': 'True'})
        },
        u'silk.response': {
            'Meta': {'object_name': 'Response'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'encoded_headers': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'request': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'response'", 'unique': 'True', 'to': u"orm['silk.Request']"}),
            'status_code': ('django.db.models.fields.IntegerField', [], {})
        },
        u'silk.sqlquery': {
            'Meta': {'object_name': 'SQLQuery'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.TextField', [], {}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'queries'", 'null': 'True', 'to': u"orm['silk.Request']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'time_taken': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'traceback': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['silk']

    depends_on = [
    ]
    
