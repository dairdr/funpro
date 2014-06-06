# -*- encoding: utf-8 -*-
"""Defines all Login's models.

Many of these modules are admin by Django Admin UI.

"""
from django.conf import settings
from django.db import models

class Teacher(models.Model):
	"""Teacher table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	lastname = models.CharField(max_length=45, db_column='lastname', null=True, blank=True)

	class Meta:
		db_table = 'dashboard_teacher'
		ordering = ['id']
		verbose_name = 'teacher'
		verbose_name_plural = 'teachers'

	def fullname(self):
		return '%s %s' % (self.name, self.lastname)

	def __unicode__(self):
		return self.fullname()

class Course(models.Model):
	"""Course table class."""
	code = models.CharField(max_length=45, db_column='code', null=True, blank=False, unique=True)
	name = models.CharField(max_length=45, db_column='name', null=True)
	teacher = models.ForeignKey(Teacher, db_column='teacher', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_course'
		ordering = ['id']
		verbose_name = 'course'
		verbose_name_plural = 'courses'

	def __unicode__(self):
		return self.name

class Season(models.Model):
	"""Season table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)

	class Meta:
		db_table = 'dashboard_season'
		ordering = ['id']
		verbose_name = 'season'
		verbose_name_plural = 'seasons'

	def __unicode__(self):
		return self.name

class StudentHasCourse(models.Model):
	"""StudentHasCourse table class."""
	student = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='student', on_delete=models.PROTECT)
	course = models.ForeignKey(Course, db_column='course', on_delete=models.PROTECT)
	season = models.ForeignKey(Season, db_column='season', on_delete=models.PROTECT)
	performance = models.DecimalField(db_column='performance', max_digits=5, decimal_places=2, default=0.0)

	class Meta:
		db_table = 'dashboard_student_has_course'
		ordering = ['id']
		verbose_name = 'student_has_course'
		verbose_name_plural = 'student_has_courses'

	def __unicode__(self):
		return '%s (%s)' % (self.student.first_name, self.course.name)

class Lesson(models.Model):
	"""Lesson table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	course = models.ForeignKey(Course, db_column='course', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_lesson'
		ordering = ['id']
		verbose_name = 'lesson'
		verbose_name_plural = 'lessons'

	def __unicode__(self):
		return self.name

class PedagogicalStrategyContext(models.Model):
	"""PedagogicalStrategyContext table class."""
	lesson = models.ForeignKey(Lesson, db_column='lesson', on_delete=models.PROTECT)
	course = models.ForeignKey(Course, db_column='course', on_delete=models.PROTECT)
	learning_style_dimension = models.ForeignKey('LearningStyleDimension', db_column='learning_style_dimension', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_pedagogical_strategy_context'
		ordering = ['id']
		verbose_name = 'pedagogical_strategy_context'
		verbose_name_plural = 'pedagogical_strategies_context'

	def __unicode__(self):
		return 'pedagogical_strategy_context'

class LearningStyle(models.Model):
	"""LearningStyle table class."""
	processing = models.CharField(max_length=45, db_column='processing', null=True)
	perception = models.CharField(max_length=45, db_column='perception', null=True)
	reception = models.CharField(max_length=45, db_column='reception', null=True)
	understanding = models.CharField(max_length=45, db_column='understanding', null=True)

	class Meta:
		db_table = 'dashboard_learning_style'
		ordering = ['id']
		verbose_name = 'learning_style'
		verbose_name_plural = 'learning_styles'

	def __unicode__(self):
		return 'learning_style'

class LearningStyleDimension(models.Model):
	"""LearningStyleDimension table class."""
	student = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='student', on_delete=models.PROTECT)
	learning_style = models.ForeignKey(LearningStyle, db_column='learning_style', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_learning_style_dimension'
		ordering = ['id']
		verbose_name = 'learning_style_dimension'
		verbose_name_plural = 'learning_styles_dimension'

	def __unicode__(self):
		return 'learning_style_dimension'

class PerformanceProfile(models.Model):
	"""PerformanceProfile table class."""
	performance = models.PositiveSmallIntegerField(db_column='performance', null=True)
	lesson = models.ForeignKey(Lesson, db_column='lesson', on_delete=models.PROTECT)
	student = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='student', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_performance_profile'
		ordering = ['id']
		verbose_name = 'performance_profile'
		verbose_name_plural = 'performance_profiles'

	def __unicode__(self):
		return self.performance

class LearningTheory(models.Model):
	"""LearningTheory table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	navigation_style = models.ForeignKey('NavigationStyle', db_column='navigation_style', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_learning_theory'
		ordering = ['id']
		verbose_name = 'learning_theory'
		verbose_name_plural = 'learning_theories'

	def __unicode__(self):
		return self.name

class PedagogicTactic(models.Model):
	"""PedagogicTactic table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	learning_resource = models.ManyToManyField('LearningResource', through='PedagogicTacticHasLearningResource')

	class Meta:
		db_table = 'dashboard_pedagogic_tactic'
		ordering = ['id']
		verbose_name = 'pedagogic_tactic'
		verbose_name_plural = 'pedagogic_tactics'

	def __unicode__(self):
		return self.name

class LessonComponent(models.Model):
	"""LessonComponent table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	pedagogic_tactic = models.ManyToManyField(PedagogicTactic, through='LessonComponentHasPedagogicTactic')

	class Meta:
		db_table = 'dashboard_lesson_component'
		ordering = ['id']
		verbose_name = 'lesson_component'
		verbose_name_plural = 'lesson_components'

	def __unicode__(self):
		return self.name

class LessonComponentHasPedagogicTactic(models.Model):
	"""LessonComponentHasPedagogicTactic table class."""
	lesson_component = models.ForeignKey(LessonComponent, db_column='lesson_component', on_delete=models.PROTECT)
	pedagogic_tactic = models.ForeignKey(PedagogicTactic, db_column='pedagogic_tactic', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_lesson_component_has_pedagogic_tactic'
		ordering = ['id']
		verbose_name = 'lesson_component_has_pedagogic_tactic'
		verbose_name_plural = 'lesson_components_has_pedagogic_tactics'

	def __unicode__(self):
		return 'lesson_component'

class TeachingMethod(models.Model):
	"""TeachingMethod table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	learning_theory = models.ForeignKey(LearningTheory, db_column='learning_theory', on_delete=models.PROTECT)
	pedagogic_tactic = models.ManyToManyField(PedagogicTactic, through='TeachingMethodHasPedagogicTactic')

	class Meta:
		db_table = 'dashboard_teaching_method'
		ordering = ['id']
		verbose_name = 'teaching_method'
		verbose_name_plural = 'teaching_methods'

	def __unicode__(self):
		return self.name

class TeachingMethodHasPedagogicTactic(models.Model):
	"""TeachingMethodHasPedagogicTactic table class"""
	teaching_method = models.ForeignKey(TeachingMethod, db_column='teaching_method', on_delete=models.PROTECT)
	pedagogic_tactic = models.ForeignKey(PedagogicTactic, db_column='pedagogic_tactic', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_teaching_method_has_pedagogic_tactic'
		ordering = ['id']
		verbose_name = 'teaching_method_has_pedagogic_tactic'
		verbose_name_plural = 'teaching_method_has_pedagogic_tactics'

	def __unicode__(self):
		return 'teaching_method_has_pedagogic_tactic'

class NavigationStyle(models.Model):
	"""NavigationStyle table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)

	class Meta:
		db_table = 'dashboard_navigation_style'
		ordering = ['id']
		verbose_name = 'navigation_style'
		verbose_name_plural = 'navigation_styles'

	def __unicode__(self):
		return self.name

class PedagogicStrategyGeneralRecommendation(models.Model):
	"""PedagogicStrategyGeneralRecommendation table class."""
	performance = models.PositiveSmallIntegerField(db_column='performance', null=True)
	pedagogical_strategy_context = models.ForeignKey(PedagogicalStrategyContext, db_column='pedagogical_strategy_context', on_delete=models.PROTECT)
	teaching_method = models.ForeignKey(TeachingMethod, db_column='teaching_method', on_delete=models.PROTECT)
	learning_theory = models.ForeignKey(LearningTheory, db_column='learning_theory', on_delete=models.PROTECT)
	status = models.BooleanField(db_column='status', default=True)
	generated = models.CharField(db_column='generated', max_length=10, default='auto')

	class Meta:
		db_table = 'dashboard_pedagogic_strategy_general_recommendation'
		ordering = ['id']
		verbose_name = 'pedagogic_strategy_general_recommendation'
		verbose_name_plural = 'pedagogic_strategy_general_recommendations'

	def __unicode__(self):
		return self.performance

class LearningResource(models.Model):
	"""LearningResource table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	url = models.TextField(db_column='url', null=True)
	lesson_component = models.ManyToManyField(LessonComponent, through='LearningResourceHasLessonComponent')

	class Meta:
		db_table = 'dashboard_learning_resource'
		ordering = ['id']
		verbose_name = 'learning_resource'
		verbose_name_plural = 'learning_resources'

	def __unicode__(self):
		return self.name

class LearningResourceHasLessonComponent(models.Model):
	"""LearningResourceHasLessonComponent table class"""
	learning_resource = models.ForeignKey(LearningResource, db_column='learning_resource', on_delete=models.PROTECT)
	lesson_component = models.ForeignKey(LessonComponent, db_column='lesson_component', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_learning_resource_has_lesson_component'
		ordering = ['id']
		verbose_name = 'learning_resource_has_lesson_component'
		verbose_name_plural = 'learning_resource_has_lesson_components'

	def __unicode__(self):
		return 'learning_resource_has_lesson_component'

class PedagogicTacticHasLearningResource(models.Model):
	"""PedagogicTacticHasLearningResource table class."""
	pedagogic_tactic = models.ForeignKey(PedagogicTactic, db_column='pedagogic_tactic', on_delete=models.PROTECT)
	learning_resource = models.ForeignKey(LearningResource, db_column='learning_resource', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_pedagogic_tactic_has_learning_resource'
		ordering = ['id']
		verbose_name = 'pedagogic_tactic_has_learning_resource'
		verbose_name_plural = 'pedagogic_tactic_has_learning_resources'

	def __unicode__(self):
		return 'pedagogic_tactic_has_learning_resource'

class PedagogicStrategySpecificRecommendation(models.Model):
	"""PedagogicStrategySpecificRecommendation table class."""
	performance = models.PositiveSmallIntegerField(db_column='performance', null=True)
	learning_resource = models.ForeignKey(LearningResource, db_column='learning_resource', on_delete=models.PROTECT)
	pedagogic_strategy_general_recommendation = models.ForeignKey(PedagogicStrategyGeneralRecommendation, db_column='pedagogic_strategy_general_recommendation', on_delete=models.PROTECT)
	lesson_component = models.ForeignKey(LessonComponent, db_column='lesson_component', on_delete=models.PROTECT)
	pedagogic_tactic = models.ForeignKey(PedagogicTactic, db_column='pedagogic_tactic', on_delete=models.PROTECT)
	status = models.BooleanField(db_column='status', default=True)
	generated = models.CharField(db_column='generated', max_length=10, default='auto')

	class Meta:
		db_table = 'dashboard_pedagogic_strategy_specific_recommendation'
		ordering = ['id']
		verbose_name = 'pedagogic_strategy_specific_recommendation'
		verbose_name_plural = 'pedagogic_strategy_specific_recommendations'

	def __unicode__(self):
		return self.performance

class StyleName(models.Model):
	"""StyleName table class."""
	name = models.CharField(db_column='name', max_length=45, null=True)

	class Meta:
		db_table = 'dashboard_style_name'
		ordering = ['id']
		verbose_name = 'style_name'
		verbose_name_plural = 'style_names'

	def __unicode__(self):
		return self.name

class Test(models.Model):
	"""Test table class."""
	pos = models.PositiveSmallIntegerField(max_length=3, db_column='pos', null=True)
	name = models.TextField(db_column='name', null=True)
	option_a = models.TextField(db_column='option_a', null=True)
	option_b = models.TextField(db_column='option_b', null=True)

	class Meta:
		db_table = 'dashboard_test'
		ordering = ['id']
		verbose_name = 'test'
		verbose_name_plural = 'tests'

	def __unicode__(self):
		return self.name

class LessonStructure(models.Model):
	"""LessonStructure table class."""
	structure = models.ForeignKey('Structure', db_column='structure', on_delete=models.PROTECT)
	lesson_component = models.ForeignKey(LessonComponent, db_column='lesson_component', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_lesson_structure'
		ordering = ['id']
		verbose_name = 'lesson_structure'
		verbose_name_plural = 'lesson_structures'

	def __unicode__(self):
		return ''

class Structure(models.Model):
	"""Structure table class."""
	name = models.CharField(max_length=45, db_column='name', null=True)
	style_name = models.ManyToManyField(StyleName, through='StructureHasStyleName')
	lesson_component = models.ManyToManyField(LessonComponent, through='StructureHasLessonComponent')

	class Meta:
		db_table = 'dashboard_structure'
		ordering = ['id']
		verbose_name = 'structure'
		verbose_name_plural = 'structures'

	def __unicode__(self):
		return self.name

class StructureHasStyleName(models.Model):
	"""StructureHasStyleName table class."""
	structure = models.ForeignKey(Structure, db_column='structure', on_delete=models.PROTECT)
	style_name = models.ForeignKey(StyleName, db_column='style_name', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_structure_has_style_name'
		ordering = ['id']
		verbose_name = 'structure_has_style_name'
		verbose_name_plural = 'structure_has_style_names'

	def __unicode__(self):
		return 'structure_has_style_name'

class StructureHasLessonComponent(models.Model):
	"""StructureHasLessonComponent table class."""
	structure = models.ForeignKey(Structure, db_column='structure', on_delete=models.PROTECT)
	lesson_component = models.ForeignKey(LessonComponent, db_column='lesson_component', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_structure_has_lesson_component'
		ordering = ['id']
		verbose_name = 'structure_has_lesson_component'
		verbose_name_plural = 'structure_has_lesson_components'

	def __unicode__(self):
		return 'structure_has_lesson_component'

class GivesSupportTo(models.Model):
	"""GivesSupportTo table class."""
	style_name = models.ForeignKey(StyleName, db_column='style_name', on_delete=models.PROTECT)
	pedagogic_tactic = models.ForeignKey(PedagogicTactic, db_column='pedagogic_tactic', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_gives_support_to'
		ordering = ['id']
		verbose_name = 'gives_support_to'
		verbose_name_plural = 'gives_support_to'

	def __unicode__(self):
		return 'gives_support_to'

class Session(models.Model):
	"""Session table class."""
	pedagogical_strategy_context = models.ForeignKey(PedagogicalStrategyContext, db_column='pedagogical_strategy_context', on_delete=models.PROTECT)
	pedagogic_strategy_specific_recommendation = models.ForeignKey(PedagogicStrategySpecificRecommendation, db_column='pedagogic_strategy_specific_recommendation', on_delete=models.PROTECT)
	created_at = models.DateTimeField(db_column='created_at', auto_now=True)
	student = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='student', on_delete=models.PROTECT)

	class Meta:
		db_table = 'dashboard_session'
		ordering = ['id']
		verbose_name = 'gives_session'
		verbose_name_plural = 'gives_sessions'

	def __unicode__(self):
		return 'session'