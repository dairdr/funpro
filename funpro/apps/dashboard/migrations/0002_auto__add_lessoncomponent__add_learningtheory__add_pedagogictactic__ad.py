# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LessonComponent'
        db.create_table('lesson_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['LessonComponent'])

        # Adding M2M table for field pedagogic_tactic on 'LessonComponent'
        m2m_table_name = db.shorten_name('lesson_component_pedagogic_tactic')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lessoncomponent', models.ForeignKey(orm[u'dashboard.lessoncomponent'], null=False)),
            ('pedagogictactic', models.ForeignKey(orm[u'dashboard.pedagogictactic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lessoncomponent_id', 'pedagogictactic_id'])

        # Adding model 'LearningTheory'
        db.create_table('learning_theory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['LearningTheory'])

        # Adding model 'PedagogicTactic'
        db.create_table('pedagogic_tactic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicTactic'])

        # Adding model 'LearningStyle'
        db.create_table('learning_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['LearningStyle'])

        # Adding model 'LearningStyleDimension'
        db.create_table('learning_style_dimension', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Lesson'], on_delete=models.PROTECT, db_column='lesson')),
            ('learning_style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningStyle'], on_delete=models.PROTECT, db_column='learning_style')),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], on_delete=models.PROTECT, db_column='student')),
        ))
        db.send_create_signal(u'dashboard', ['LearningStyleDimension'])

        # Adding model 'PerformanceProfile'
        db.create_table('performance_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, db_column='performance')),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Lesson'], on_delete=models.PROTECT, db_column='lesson')),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], on_delete=models.PROTECT, db_column='student')),
        ))
        db.send_create_signal(u'dashboard', ['PerformanceProfile'])

        # Adding model 'PedagogicalStrategyContext'
        db.create_table('pedagogical_strategy_context', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Lesson'], on_delete=models.PROTECT, db_column='lesson')),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Course'], on_delete=models.PROTECT, db_column='course')),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], on_delete=models.PROTECT, db_column='student')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicalStrategyContext'])

        # Adding model 'Lesson'
        db.create_table('lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='45', null=True, db_column='name')),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Course'], on_delete=models.PROTECT, db_column='course')),
        ))
        db.send_create_signal(u'dashboard', ['Lesson'])

        # Adding M2M table for field lesson_component on 'Lesson'
        m2m_table_name = db.shorten_name('lesson_lesson_component')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm[u'dashboard.lesson'], null=False)),
            ('lessoncomponent', models.ForeignKey(orm[u'dashboard.lessoncomponent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lesson_id', 'lessoncomponent_id'])


    def backwards(self, orm):
        # Deleting model 'LessonComponent'
        db.delete_table('lesson_component')

        # Removing M2M table for field pedagogic_tactic on 'LessonComponent'
        db.delete_table(db.shorten_name('lesson_component_pedagogic_tactic'))

        # Deleting model 'LearningTheory'
        db.delete_table('learning_theory')

        # Deleting model 'PedagogicTactic'
        db.delete_table('pedagogic_tactic')

        # Deleting model 'LearningStyle'
        db.delete_table('learning_style')

        # Deleting model 'LearningStyleDimension'
        db.delete_table('learning_style_dimension')

        # Deleting model 'PerformanceProfile'
        db.delete_table('performance_profile')

        # Deleting model 'PedagogicalStrategyContext'
        db.delete_table('pedagogical_strategy_context')

        # Deleting model 'Lesson'
        db.delete_table('lesson')

        # Removing M2M table for field lesson_component on 'Lesson'
        db.delete_table(db.shorten_name('lesson_lesson_component'))


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
        u'dashboard.pedagogicalstrategycontext': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicalStrategyContext', 'db_table': "'pedagogical_strategy_context'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Course']", 'on_delete': 'models.PROTECT', 'db_column': "'course'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Lesson']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'45'", 'null': 'True', 'db_column': "'name'"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'on_delete': 'models.PROTECT', 'db_column': "'student'"})
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
        }
    }

    complete_apps = ['dashboard']