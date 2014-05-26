# -*- encoding: utf-8 -*-
"""Defines all models to admin for Django Admin UI."""
from django.contrib import admin
from models import *

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(PedagogicalStrategyContext)
admin.site.register(LearningStyle)
admin.site.register(LearningStyleDimension)
admin.site.register(PerformanceProfile)
admin.site.register(LearningTheory)
admin.site.register(PedagogicTactic)
admin.site.register(LessonComponent)
admin.site.register(TeachingMethod)
admin.site.register(NavigationStyle)
admin.site.register(PedagogicStrategyGeneralRecommendation)
admin.site.register(LearningResource)
admin.site.register(PedagogicStrategySpecificRecommendation)
admin.site.register(Test)