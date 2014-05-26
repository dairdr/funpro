# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Test.pos'
        db.add_column('test', 'pos',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3, null=True, db_column='pos'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Test.pos'
        db.delete_column('test', 'pos')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dashboard.course': {
            'Meta': {'ordering': "['id']", 'object_name': 'Course', 'db_table': "'course'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Teacher']", 'on_delete': 'models.PROTECT', 'db_column': "'teacher'"})
        },
        u'dashboard.learningresource': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningResource', 'db_table': "'learning_resource'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboard.PedagogicTactic']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': "'500'", 'null': 'True', 'db_column': "'url'"})
        },
        u'dashboard.learningstyle': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningStyle', 'db_table': "'learning_style'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.learningstyledimension': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningStyleDimension', 'db_table': "'learning_style_dimension'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningStyle']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_style'"}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Lesson']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'on_delete': 'models.PROTECT', 'db_column': "'student'"})
        },
        u'dashboard.learningtheory': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningTheory', 'db_table': "'learning_theory'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.lesson': {
            'Meta': {'ordering': "['id']", 'object_name': 'Lesson', 'db_table': "'lesson'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Course']", 'on_delete': 'models.PROTECT', 'db_column': "'course'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson_component': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboard.LessonComponent']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.lessoncomponent': {
            'Meta': {'ordering': "['id']", 'object_name': 'LessonComponent', 'db_table': "'lesson_component'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboard.PedagogicTactic']", 'symmetrical': 'False'})
        },
        u'dashboard.navigationstyle': {
            'Meta': {'ordering': "['id']", 'object_name': 'NavigationStyle', 'db_table': "'navigation_style'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.pedagogicalstrategycontext': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicalStrategyContext', 'db_table': "'pedagogical_strategy_context'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Course']", 'on_delete': 'models.PROTECT', 'db_column': "'course'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Lesson']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'on_delete': 'models.PROTECT', 'db_column': "'student'"})
        },
        u'dashboard.pedagogicstrategygeneralrecommendation': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicStrategyGeneralRecommendation', 'db_table': "'pedagogic_strategy_general_recommendation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_theorie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningTheory']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_theorie'"}),
            'navigation_style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.NavigationStyle']", 'on_delete': 'models.PROTECT', 'db_column': "'navigation_style'"}),
            'pedagogical_strategy_context': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicalStrategyContext']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogical_strategy_context'"}),
            'performance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'db_column': "'performance'"}),
            'teaching_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.TeachingMethod']", 'on_delete': 'models.PROTECT', 'db_column': "'teaching_method'"})
        },
        u'dashboard.pedagogicstrategyspecificrecommendation': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicStrategySpecificRecommendation', 'db_table': "'pedagogic_strategy_specific_recommendation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningResource']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_resource'"}),
            'lesson_component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LessonComponent']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson_component'"}),
            'pedagogic_strategy_general_recommendation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicStrategyGeneralRecommendation']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_strategy_general_recommendation'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicTactic']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_tactic'"}),
            'performance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'db_column': "'performance'"})
        },
        u'dashboard.pedagogictactic': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicTactic', 'db_table': "'pedagogic_tactic'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.performanceprofile': {
            'Meta': {'ordering': "['id']", 'object_name': 'PerformanceProfile', 'db_table': "'performance_profile'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Lesson']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson'"}),
            'performance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'db_column': "'performance'"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'on_delete': 'models.PROTECT', 'db_column': "'student'"})
        },
        u'dashboard.teacher': {
            'Meta': {'ordering': "['id']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'lastname'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.teachingmethod': {
            'Meta': {'ordering': "['id']", 'object_name': 'TeachingMethod', 'db_table': "'teaching_method'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_theory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningTheory']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_theory'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboard.PedagogicTactic']", 'symmetrical': 'False'})
        },
        u'dashboard.test': {
            'Meta': {'ordering': "['id']", 'object_name': 'Test', 'db_table': "'test'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': "'300'", 'null': 'True', 'db_column': "'name'"}),
            'option_a': ('django.db.models.fields.TextField', [], {'max_length': "'300'", 'null': 'True', 'db_column': "'option_a'"}),
            'option_b': ('django.db.models.fields.TextField', [], {'max_length': "'300'", 'null': 'True', 'db_column': "'option_b'"}),
            'pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'db_column': "'pos'"})
        }
    }

    complete_apps = ['dashboard']