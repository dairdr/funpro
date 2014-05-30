# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teacher'
        db.create_table('dashboard_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='lastname', blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['Teacher'])

        # Adding model 'Course'
        db.create_table('dashboard_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Teacher'], on_delete=models.PROTECT, db_column='teacher')),
        ))
        db.send_create_signal(u'dashboard', ['Course'])

        # Adding model 'StudentHasCourse'
        db.create_table('dashboard_student_has_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Student'], on_delete=models.PROTECT, db_column='student')),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Course'], on_delete=models.PROTECT, db_column='course')),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='season')),
            ('performance', self.gf('django.db.models.fields.DecimalField')(null=True, db_column='performance', decimal_places=2, max_digits=5)),
        ))
        db.send_create_signal(u'dashboard', ['StudentHasCourse'])

        # Adding model 'Lesson'
        db.create_table('dashboard_lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Course'], on_delete=models.PROTECT, db_column='course')),
        ))
        db.send_create_signal(u'dashboard', ['Lesson'])

        # Adding model 'PedagogicalStrategyContext'
        db.create_table('dashboard_pedagogical_strategy_context', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Lesson'], on_delete=models.PROTECT, db_column='lesson')),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Course'], on_delete=models.PROTECT, db_column='course')),
            ('learning_style_dimension', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningStyleDimension'], on_delete=models.PROTECT, db_column='learning_style_dimension')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicalStrategyContext'])

        # Adding model 'LearningStyle'
        db.create_table('dashboard_learning_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('processing', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='processing')),
            ('perception', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='perception')),
            ('reception', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='reception')),
            ('understanding', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='understanding')),
        ))
        db.send_create_signal(u'dashboard', ['LearningStyle'])

        # Adding model 'LearningStyleDimension'
        db.create_table('dashboard_learning_style_dimension', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Student'], on_delete=models.PROTECT, db_column='student')),
            ('learning_style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningStyle'], on_delete=models.PROTECT, db_column='learning_style')),
        ))
        db.send_create_signal(u'dashboard', ['LearningStyleDimension'])

        # Adding model 'PerformanceProfile'
        db.create_table('dashboard_performance_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, db_column='performance')),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Lesson'], on_delete=models.PROTECT, db_column='lesson')),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Student'], on_delete=models.PROTECT, db_column='student')),
        ))
        db.send_create_signal(u'dashboard', ['PerformanceProfile'])

        # Adding model 'LearningTheory'
        db.create_table('dashboard_learning_theory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
            ('navigation_style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.NavigationStyle'], on_delete=models.PROTECT, db_column='navigation_style')),
        ))
        db.send_create_signal(u'dashboard', ['LearningTheory'])

        # Adding model 'PedagogicTactic'
        db.create_table('dashboard_pedagogic_tactic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicTactic'])

        # Adding model 'LessonComponent'
        db.create_table('dashboard_lesson_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['LessonComponent'])

        # Adding model 'LessonComponentHasPedagogicTactic'
        db.create_table('dashboard_lesson_component_has_pedagogic_tactic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lesson_component', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LessonComponent'], on_delete=models.PROTECT, db_column='lesson_component')),
            ('pedagogic_tactic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicTactic'], on_delete=models.PROTECT, db_column='pedagogic_tactic')),
        ))
        db.send_create_signal(u'dashboard', ['LessonComponentHasPedagogicTactic'])

        # Adding model 'TeachingMethod'
        db.create_table('dashboard_teaching_method', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
            ('learning_theory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningTheory'], on_delete=models.PROTECT, db_column='learning_theory')),
        ))
        db.send_create_signal(u'dashboard', ['TeachingMethod'])

        # Adding model 'TeachingMethodHasPedagogicTactic'
        db.create_table('dashboard_teaching_method_has_pedagogic_tactic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teaching_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.TeachingMethod'], on_delete=models.PROTECT, db_column='teaching_method')),
            ('pedagogic_tactic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicTactic'], on_delete=models.PROTECT, db_column='pedagogic_tactic')),
        ))
        db.send_create_signal(u'dashboard', ['TeachingMethodHasPedagogicTactic'])

        # Adding model 'NavigationStyle'
        db.create_table('dashboard_navigation_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['NavigationStyle'])

        # Adding model 'PedagogicStrategyGeneralRecommendation'
        db.create_table('dashboard_pedagogic_strategy_general_recommendation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, db_column='performance')),
            ('pedagogical_strategy_context', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicalStrategyContext'], on_delete=models.PROTECT, db_column='pedagogical_strategy_context')),
            ('teaching_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.TeachingMethod'], on_delete=models.PROTECT, db_column='teaching_method')),
            ('learning_theory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningTheory'], on_delete=models.PROTECT, db_column='learning_theory')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicStrategyGeneralRecommendation'])

        # Adding model 'LearningResource'
        db.create_table('dashboard_learning_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
            ('url', self.gf('django.db.models.fields.TextField')(null=True, db_column='url')),
        ))
        db.send_create_signal(u'dashboard', ['LearningResource'])

        # Adding model 'PedagogicTacticHasLearningResource'
        db.create_table('dashboard_pedagogic_tactic_has_learning_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pedagogic_tactic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicTactic'], on_delete=models.PROTECT, db_column='pedagogic_tactic')),
            ('learning_resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningResource'], on_delete=models.PROTECT, db_column='learning_resource')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicTacticHasLearningResource'])

        # Adding model 'PedagogicStrategySpecificRecommendation'
        db.create_table('dashboard_pedagogic_strategy_specific_recommendation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performance', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, db_column='performance')),
            ('learning_resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LearningResource'], on_delete=models.PROTECT, db_column='learning_resource')),
            ('pedagogic_strategy_general_recommendation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicStrategyGeneralRecommendation'], on_delete=models.PROTECT, db_column='pedagogic_strategy_general_recommendation')),
            ('lesson_component', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LessonComponent'], on_delete=models.PROTECT, db_column='lesson_component')),
            ('pedagogic_tactic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicTactic'], on_delete=models.PROTECT, db_column='pedagogic_tactic')),
        ))
        db.send_create_signal(u'dashboard', ['PedagogicStrategySpecificRecommendation'])

        # Adding model 'StyleName'
        db.create_table('dashboard_style_name', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, null=True, db_column='name')),
        ))
        db.send_create_signal(u'dashboard', ['StyleName'])

        # Adding model 'Test'
        db.create_table('dashboard_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3, null=True, db_column='pos')),
            ('name', self.gf('django.db.models.fields.TextField')(null=True, db_column='name')),
            ('option_a', self.gf('django.db.models.fields.TextField')(null=True, db_column='option_a')),
            ('option_b', self.gf('django.db.models.fields.TextField')(null=True, db_column='option_b')),
        ))
        db.send_create_signal(u'dashboard', ['Test'])

        # Adding model 'LessonStructure'
        db.create_table('dashboard_lesson_structure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.Structure'], on_delete=models.PROTECT, db_column='structure')),
            ('lesson_component', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.LessonComponent'], on_delete=models.PROTECT, db_column='lesson_component')),
        ))
        db.send_create_signal(u'dashboard', ['LessonStructure'])

        # Adding model 'Structure'
        db.create_table('dashboard_structure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('style_value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.StyleName'], on_delete=models.PROTECT, db_column='style_value')),
        ))
        db.send_create_signal(u'dashboard', ['Structure'])

        # Adding model 'GivesSupportTo'
        db.create_table('dashboard_gives_support_to', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('style_value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.StyleName'], on_delete=models.PROTECT, db_column='style_value')),
            ('pedagogic_tactic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.PedagogicTactic'], on_delete=models.PROTECT, db_column='pedagogic_tactic')),
        ))
        db.send_create_signal(u'dashboard', ['GivesSupportTo'])


    def backwards(self, orm):
        # Deleting model 'Teacher'
        db.delete_table('dashboard_teacher')

        # Deleting model 'Course'
        db.delete_table('dashboard_course')

        # Deleting model 'StudentHasCourse'
        db.delete_table('dashboard_student_has_course')

        # Deleting model 'Lesson'
        db.delete_table('dashboard_lesson')

        # Deleting model 'PedagogicalStrategyContext'
        db.delete_table('dashboard_pedagogical_strategy_context')

        # Deleting model 'LearningStyle'
        db.delete_table('dashboard_learning_style')

        # Deleting model 'LearningStyleDimension'
        db.delete_table('dashboard_learning_style_dimension')

        # Deleting model 'PerformanceProfile'
        db.delete_table('dashboard_performance_profile')

        # Deleting model 'LearningTheory'
        db.delete_table('dashboard_learning_theory')

        # Deleting model 'PedagogicTactic'
        db.delete_table('dashboard_pedagogic_tactic')

        # Deleting model 'LessonComponent'
        db.delete_table('dashboard_lesson_component')

        # Deleting model 'LessonComponentHasPedagogicTactic'
        db.delete_table('dashboard_lesson_component_has_pedagogic_tactic')

        # Deleting model 'TeachingMethod'
        db.delete_table('dashboard_teaching_method')

        # Deleting model 'TeachingMethodHasPedagogicTactic'
        db.delete_table('dashboard_teaching_method_has_pedagogic_tactic')

        # Deleting model 'NavigationStyle'
        db.delete_table('dashboard_navigation_style')

        # Deleting model 'PedagogicStrategyGeneralRecommendation'
        db.delete_table('dashboard_pedagogic_strategy_general_recommendation')

        # Deleting model 'LearningResource'
        db.delete_table('dashboard_learning_resource')

        # Deleting model 'PedagogicTacticHasLearningResource'
        db.delete_table('dashboard_pedagogic_tactic_has_learning_resource')

        # Deleting model 'PedagogicStrategySpecificRecommendation'
        db.delete_table('dashboard_pedagogic_strategy_specific_recommendation')

        # Deleting model 'StyleName'
        db.delete_table('dashboard_style_name')

        # Deleting model 'Test'
        db.delete_table('dashboard_test')

        # Deleting model 'LessonStructure'
        db.delete_table('dashboard_lesson_structure')

        # Deleting model 'Structure'
        db.delete_table('dashboard_structure')

        # Deleting model 'GivesSupportTo'
        db.delete_table('dashboard_gives_support_to')


    models = {
        u'account.student': {
            'Meta': {'ordering': "['id']", 'object_name': 'Student'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_column': "'date_joined'"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_of_birth'"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_column': "'email'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'first_name'"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'is_active'"}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'is_staff'"}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'last_name'", 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dashboard.course': {
            'Meta': {'ordering': "['id']", 'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Teacher']", 'on_delete': 'models.PROTECT', 'db_column': "'teacher'"})
        },
        u'dashboard.givessupportto': {
            'Meta': {'ordering': "['id']", 'object_name': 'GivesSupportTo', 'db_table': "'dashboard_gives_support_to'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pedagogic_tactic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicTactic']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_tactic'"}),
            'style_value': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.StyleName']", 'on_delete': 'models.PROTECT', 'db_column': "'style_value'"})
        },
        u'dashboard.learningresource': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningResource', 'db_table': "'dashboard_learning_resource'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'url'"})
        },
        u'dashboard.learningstyle': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningStyle', 'db_table': "'dashboard_learning_style'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perception': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'perception'"}),
            'processing': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'processing'"}),
            'reception': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'reception'"}),
            'understanding': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'understanding'"})
        },
        u'dashboard.learningstyledimension': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningStyleDimension', 'db_table': "'dashboard_learning_style_dimension'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningStyle']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_style'"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Student']", 'on_delete': 'models.PROTECT', 'db_column': "'student'"})
        },
        u'dashboard.learningtheory': {
            'Meta': {'ordering': "['id']", 'object_name': 'LearningTheory', 'db_table': "'dashboard_learning_theory'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"}),
            'navigation_style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.NavigationStyle']", 'on_delete': 'models.PROTECT', 'db_column': "'navigation_style'"})
        },
        u'dashboard.lesson': {
            'Meta': {'ordering': "['id']", 'object_name': 'Lesson'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Course']", 'on_delete': 'models.PROTECT', 'db_column': "'course'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.lessoncomponent': {
            'Meta': {'ordering': "['id']", 'object_name': 'LessonComponent', 'db_table': "'dashboard_lesson_component'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboard.PedagogicTactic']", 'through': u"orm['dashboard.LessonComponentHasPedagogicTactic']", 'symmetrical': 'False'})
        },
        u'dashboard.lessoncomponenthaspedagogictactic': {
            'Meta': {'ordering': "['id']", 'object_name': 'LessonComponentHasPedagogicTactic', 'db_table': "'dashboard_lesson_component_has_pedagogic_tactic'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson_component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LessonComponent']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson_component'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicTactic']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_tactic'"})
        },
        u'dashboard.lessonstructure': {
            'Meta': {'ordering': "['id']", 'object_name': 'LessonStructure', 'db_table': "'dashboard_lesson_structure'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson_component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LessonComponent']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson_component'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Structure']", 'on_delete': 'models.PROTECT', 'db_column': "'structure'"})
        },
        u'dashboard.navigationstyle': {
            'Meta': {'ordering': "['id']", 'object_name': 'NavigationStyle', 'db_table': "'dashboard_navigation_style'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.pedagogicalstrategycontext': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicalStrategyContext', 'db_table': "'dashboard_pedagogical_strategy_context'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Course']", 'on_delete': 'models.PROTECT', 'db_column': "'course'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_style_dimension': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningStyleDimension']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_style_dimension'"}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Lesson']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson'"})
        },
        u'dashboard.pedagogicstrategygeneralrecommendation': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicStrategyGeneralRecommendation', 'db_table': "'dashboard_pedagogic_strategy_general_recommendation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_theory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningTheory']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_theory'"}),
            'pedagogical_strategy_context': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicalStrategyContext']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogical_strategy_context'"}),
            'performance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'db_column': "'performance'"}),
            'teaching_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.TeachingMethod']", 'on_delete': 'models.PROTECT', 'db_column': "'teaching_method'"})
        },
        u'dashboard.pedagogicstrategyspecificrecommendation': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicStrategySpecificRecommendation', 'db_table': "'dashboard_pedagogic_strategy_specific_recommendation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningResource']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_resource'"}),
            'lesson_component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LessonComponent']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson_component'"}),
            'pedagogic_strategy_general_recommendation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicStrategyGeneralRecommendation']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_strategy_general_recommendation'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicTactic']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_tactic'"}),
            'performance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'db_column': "'performance'"})
        },
        u'dashboard.pedagogictactic': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicTactic', 'db_table': "'dashboard_pedagogic_tactic'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_resource': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboard.LearningResource']", 'through': u"orm['dashboard.PedagogicTacticHasLearningResource']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.pedagogictactichaslearningresource': {
            'Meta': {'ordering': "['id']", 'object_name': 'PedagogicTacticHasLearningResource', 'db_table': "'dashboard_pedagogic_tactic_has_learning_resource'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningResource']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_resource'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicTactic']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_tactic'"})
        },
        u'dashboard.performanceprofile': {
            'Meta': {'ordering': "['id']", 'object_name': 'PerformanceProfile', 'db_table': "'dashboard_performance_profile'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Lesson']", 'on_delete': 'models.PROTECT', 'db_column': "'lesson'"}),
            'performance': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'db_column': "'performance'"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Student']", 'on_delete': 'models.PROTECT', 'db_column': "'student'"})
        },
        u'dashboard.structure': {
            'Meta': {'ordering': "['id']", 'object_name': 'Structure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'style_value': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.StyleName']", 'on_delete': 'models.PROTECT', 'db_column': "'style_value'"})
        },
        u'dashboard.studenthascourse': {
            'Meta': {'ordering': "['id']", 'object_name': 'StudentHasCourse', 'db_table': "'dashboard_student_has_course'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Course']", 'on_delete': 'models.PROTECT', 'db_column': "'course'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'performance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'db_column': "'performance'", 'decimal_places': '2', 'max_digits': '5'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'season'"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Student']", 'on_delete': 'models.PROTECT', 'db_column': "'student'"})
        },
        u'dashboard.stylename': {
            'Meta': {'ordering': "['id']", 'object_name': 'StyleName', 'db_table': "'dashboard_style_name'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.teacher': {
            'Meta': {'ordering': "['id']", 'object_name': 'Teacher'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'lastname'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"})
        },
        u'dashboard.teachingmethod': {
            'Meta': {'ordering': "['id']", 'object_name': 'TeachingMethod', 'db_table': "'dashboard_teaching_method'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learning_theory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.LearningTheory']", 'on_delete': 'models.PROTECT', 'db_column': "'learning_theory'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'db_column': "'name'"}),
            'pedagogic_tactic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboard.PedagogicTactic']", 'through': u"orm['dashboard.TeachingMethodHasPedagogicTactic']", 'symmetrical': 'False'})
        },
        u'dashboard.teachingmethodhaspedagogictactic': {
            'Meta': {'ordering': "['id']", 'object_name': 'TeachingMethodHasPedagogicTactic', 'db_table': "'dashboard_teaching_method_has_pedagogic_tactic'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pedagogic_tactic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.PedagogicTactic']", 'on_delete': 'models.PROTECT', 'db_column': "'pedagogic_tactic'"}),
            'teaching_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.TeachingMethod']", 'on_delete': 'models.PROTECT', 'db_column': "'teaching_method'"})
        },
        u'dashboard.test': {
            'Meta': {'ordering': "['id']", 'object_name': 'Test'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'name'"}),
            'option_a': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'option_a'"}),
            'option_b': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'option_b'"}),
            'pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'db_column': "'pos'"})
        }
    }

    complete_apps = ['dashboard']