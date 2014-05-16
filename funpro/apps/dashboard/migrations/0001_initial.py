# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teacher'
        db.create_table('teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='lastname', blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['Teacher'])

        # Adding model 'Course'
        db.create_table('course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Teacher'], on_delete=models.PROTECT, db_column='teacher')),
        ))
        db.send_create_signal(u'dashboard', ['Course'])


    def backwards(self, orm):
        # Deleting model 'Teacher'
        db.delete_table('teacher')

        # Deleting model 'Course'
        db.delete_table('course')


    models = {
        u'dashboard.course': {
            'Meta': {'ordering': "['id']", 'object_name': 'Course', 'db_table': "'course'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Teacher']", 'on_delete': 'models.PROTECT', 'db_column': "'teacher'"})
        },
        u'dashboard.teacher': {
            'Meta': {'ordering': "['id']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'lastname'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"})
        }
    }

    complete_apps = ['dashboard']