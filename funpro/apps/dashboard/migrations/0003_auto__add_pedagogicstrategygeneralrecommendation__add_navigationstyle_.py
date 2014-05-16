# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PedagogicStrategyGeneralRecommendation'
        db.create_table('pedagogic_strategy_general_recommendation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, db_column='performance')),
            ('pedagogical_strategy_context', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicalStrategyContext'], on_delete=models.PROTECT, db_column='pedagogical_strategy_context')),
            ('teaching_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.TeachingMethod'], on_delete=models.PROTECT, db_column='teaching_method')),
            ('learning_theorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningTheory'], on_delete=models.PROTECT, db_column='learning_theorie')),
            ('navigation_style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.NavigationStyle'], on_delete=models.PROTECT, db_column='navigation_style')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicStrategyGeneralRecommendation'])

        # Adding model 'NavigationStyle'
        db.create_table('navigation_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['NavigationStyle'])

        # Adding model 'PedagogicStrategySpecificRecommendation'
        db.create_table('pedagogic_strategy_specific_recommendation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, db_column='performance')),
            ('learning_resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningResource'], on_delete=models.PROTECT, db_column='learning_resource')),
            ('pedagogic_strategy_general_recommendation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicStrategyGeneralRecommendation'], on_delete=models.PROTECT, db_column='pedagogic_strategy_general_recommendation')),
            ('lesson_component', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LessonComponent'], on_delete=models.PROTECT, db_column='lesson_component')),
            ('pedagogic_tactic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicTactic'], on_delete=models.PROTECT, db_column='pedagogic_tactic')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicStrategySpecificRecommendation'])

        # Adding model 'TeachingMethod'
        db.create_table('teaching_method', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
            ('learning_theory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningTheory'], on_delete=models.PROTECT, db_column='learning_theory')),
        ))
        db.send_create_signal(u'dashboard', ['TeachingMethod'])

        # Adding M2M table for field pedagogic_tactic on 'TeachingMethod'
        m2m_table_name = db.shorten_name('teaching_method_pedagogic_tactic')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teachingmethod', models.ForeignKey(orm[u'dashboard.teachingmethod'], null=False)),
            ('pedagogictactic', models.ForeignKey(orm[u'dashboard.pedagogictactic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['teachingmethod_id', 'pedagogictactic_id'])

        # Adding model 'LearningResource'
        db.create_table('learning_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
            ('url', self.gf('django.db.models.fields.CharField')(max_length='500', null=True, db_column='url')),
        ))
        db.send_create_signal(u'dashboard', ['LearningResource'])

        # Adding M2M table for field pedagogic_tactic on 'LearningResource'
        m2m_table_name = db.shorten_name('learning_resource_pedagogic_tactic')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('learningresource', models.ForeignKey(orm[u'dashboard.learningresource'], null=False)),
            ('pedagogictactic', models.ForeignKey(orm[u'dashboard.pedagogictactic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['learningresource_id', 'pedagogictactic_id'])


    def backwards(self, orm):
        # Deleting model 'PedagogicStrategyGeneralRecommendation'
        db.delete_table('pedagogic_strategy_general_recommendation')

        # Deleting model 'NavigationStyle'
        db.delete_table('navigation_style')

        # Deleting model 'PedagogicStrategySpecificRecommendation'
        db.delete_table('pedagogic_strategy_specific_recommendation')

        # Deleting model 'TeachingMethod'
        db.delete_table('teaching_method')

        # Removing M2M table for field pedagogic_tactic on 'TeachingMethod'
        db.delete_table(db.shorten_name('teaching_method_pedagogic_tactic'))

        # Deleting model 'LearningResource'
        db.delete_table('learning_resource')

        # Removing M2M table for field pedagogic_tactic on 'LearningResource'
        db.delete_table(db.shorten_name('learning_resource_pedagogic_tactic'))


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
        }
    }

    complete_apps = ['dashboard']