# -*- encoding: utf-8 -*-
"""Defines all Login's models.

Many of these modules are admin by Django Admin UI.

"""
from django.contrib.auth.models import User as Student
from django.db import models

class Teacher(models.Model):
	"""Teacher table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	lastname = models.CharField(max_length='45', db_column='lastname', null=True, blank=True)

	class Meta:
		db_table = 'teacher'
		ordering = ['id']
		verbose_name = 'teacher'
		verbose_name_plural = 'teachers'

	def fullname(self):
		return '%s %s' % (self.name, self.lastname)

	def __unicode__(self):
		return self.fullname()

class Course(models.Model):
	"""Course table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	teacher = models.ForeignKey(Teacher, db_column='teacher', on_delete=models.PROTECT)

	class Meta:
		db_table = 'course'
		ordering = ['id']
		verbose_name = 'course'
		verbose_name_plural = 'courses'

	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	"""Lesson table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	course = models.ForeignKey(Course, db_column='course', on_delete=models.PROTECT)
	lesson_component = models.ManyToManyField('LessonComponent')

	class Meta:
		db_table = 'lesson'
		ordering = ['id']
		verbose_name = 'lesson'
		verbose_name_plural = 'lessons'

	def __unicode__(self):
		return self.name

class PedagogicalStrategyContext(models.Model):
	"""PedagogicalStrategyContext table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	lesson = models.ForeignKey(Lesson, db_column='lesson', on_delete=models.PROTECT)
	course = models.ForeignKey(Course, db_column='course', on_delete=models.PROTECT)
	student = models.ForeignKey(Student, db_column='student', on_delete=models.PROTECT)

	class Meta:
		db_table = 'pedagogical_strategy_context'
		ordering = ['id']
		verbose_name = 'pedagogical_strategy_context'
		verbose_name_plural = 'pedagogical_strategies_context'

	def __unicode__(self):
		return self.name

class LearningStyle(models.Model):
	"""LearningStyle table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)

	class Meta:
		db_table = 'learning_style'
		ordering = ['id']
		verbose_name = 'learning_style'
		verbose_name_plural = 'learning_styles'

	def __unicode__(self):
		return self.name

class LearningStyleDimension(models.Model):
	"""LearningStyleDimension table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	lesson = models.ForeignKey(Lesson, db_column='lesson', on_delete=models.PROTECT)
	learning_style = models.ForeignKey(LearningStyle, db_column='learning_style', on_delete=models.PROTECT)
	student = models.ForeignKey(Student, db_column='student', on_delete=models.PROTECT)

	class Meta:
		db_table = 'learning_style_dimension'
		ordering = ['id']
		verbose_name = 'learning_style_dimension'
		verbose_name_plural = 'learning_styles_dimension'

	def __unicode__(self):
		return self.name

class PerformanceProfile(models.Model):
	"""PerformanceProfile table class."""
	performance = models.PositiveSmallIntegerField(db_column='performance', null=True, blank=False)
	lesson = models.ForeignKey(Lesson, db_column='lesson', on_delete=models.PROTECT)
	student = models.ForeignKey(Student, db_column='student', on_delete=models.PROTECT)

	class Meta:
		db_table = 'performance_profile'
		ordering = ['id']
		verbose_name = 'performance_profile'
		verbose_name_plural = 'performance_profiles'

	def __unicode__(self):
		return self.performance

class LearningTheory(models.Model):
	"""LearningTheory table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)

	class Meta:
		db_table = 'learning_theory'
		ordering = ['id']
		verbose_name = 'learning_theory'
		verbose_name_plural = 'learning_theories'

	def __unicode__(self):
		return self.name

class PedagogicTactic(models.Model):
	"""PedagogicTactic table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)

	class Meta:
		db_table = 'pedagogic_tactic'
		ordering = ['id']
		verbose_name = 'pedagogic_tactic'
		verbose_name_plural = 'pedagogic_tactics'

	def __unicode__(self):
		return self.name

class LessonComponent(models.Model):
	"""LessonComponent table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	pedagogic_tactic = models.ManyToManyField(PedagogicTactic)

	class Meta:
		db_table = 'lesson_component'
		ordering = ['id']
		verbose_name = 'lesson_component'
		verbose_name_plural = 'lesson_components'

	def __unicode__(self):
		return self.name

class TeachingMethod(models.Model):
	"""TeachingMethod table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	learning_theory = models.ForeignKey(LearningTheory, db_column='learning_theory', on_delete=models.PROTECT)
	pedagogic_tactic = models.ManyToManyField(PedagogicTactic)

	class Meta:
		db_table = 'teaching_method'
		ordering = ['id']
		verbose_name = 'teaching_method'
		verbose_name_plural = 'teaching_methods'

	def __unicode__(self):
		return self.name

class NavigationStyle(models.Model):
	"""NavigationStyle table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)

	class Meta:
		db_table = 'navigation_style'
		ordering = ['id']
		verbose_name = 'navigation_style'
		verbose_name_plural = 'navigation_styles'

	def __unicode__(self):
		return self.name

class PedagogicStrategyGeneralRecommendation(models.Model):
	"""PedagogicStrategyGeneralRecommendation table class."""
	performance = models.PositiveSmallIntegerField(db_column='performance', null=True, blank=False)
	pedagogical_strategy_context = models.ForeignKey(PedagogicalStrategyContext, db_column='pedagogical_strategy_context', on_delete=models.PROTECT)
	teaching_method = models.ForeignKey(TeachingMethod, db_column='teaching_method', on_delete=models.PROTECT)
	learning_theorie = models.ForeignKey(LearningTheory, db_column='learning_theorie', on_delete=models.PROTECT)
	navigation_style = models.ForeignKey(NavigationStyle, db_column='navigation_style', on_delete=models.PROTECT)

	class Meta:
		db_table = 'pedagogic_strategy_general_recommendation'
		ordering = ['id']
		verbose_name = 'pedagogic_strategy_general_recommendation'
		verbose_name_plural = 'pedagogic_strategy_general_recommendations'

	def __unicode__(self):
		return self.performance

class LearningResource(models.Model):
	"""LearningResource table class."""
	name = models.CharField(max_length='45', db_column='name', null=True, blank=False)
	url = models.CharField(max_length='500', db_column='url', null=True, blank=False)
	pedagogic_tactic = models.ManyToManyField(PedagogicTactic)

	class Meta:
		db_table = 'learning_resource'
		ordering = ['id']
		verbose_name = 'learning_resource'
		verbose_name_plural = 'learning_resources'

	def __unicode__(self):
		return self.name

class PedagogicStrategySpecificRecommendation(models.Model):
	"""PedagogicStrategySpecificRecommendation table class."""
	performance = models.PositiveSmallIntegerField(db_column='performance', null=True, blank=False)
	learning_resource = models.ForeignKey(LearningResource, db_column='learning_resource', on_delete=models.PROTECT)
	pedagogic_strategy_general_recommendation = models.ForeignKey(PedagogicStrategyGeneralRecommendation, db_column='pedagogic_strategy_general_recommendation', on_delete=models.PROTECT)
	lesson_component = models.ForeignKey(LessonComponent, db_column='lesson_component', on_delete=models.PROTECT)
	pedagogic_tactic = models.ForeignKey(PedagogicTactic, db_column='pedagogic_tactic', on_delete=models.PROTECT)

	class Meta:
		db_table = 'pedagogic_strategy_specific_recommendation'
		ordering = ['id']
		verbose_name = 'pedagogic_strategy_specific_recommendation'
		verbose_name_plural = 'pedagogic_strategy_specific_recommendations'

	def __unicode__(self):
		return self.performance