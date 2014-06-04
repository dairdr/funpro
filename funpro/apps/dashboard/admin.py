# -*- encoding: utf-8 -*-
"""Defines all models to admin for Django Admin UI."""
from django.contrib import admin
from models import *

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(StudentHasCourse)
admin.site.register(Lesson)
admin.site.register(Season)
admin.site.register(PedagogicalStrategyContext)
admin.site.register(LearningStyle)
admin.site.register(LearningStyleDimension)
admin.site.register(PerformanceProfile)
admin.site.register(LearningTheory)

admin.site.register(PedagogicTactic)
admin.site.register(LessonComponent)
admin.site.register(LessonComponentHasPedagogicTactic)

admin.site.register(TeachingMethod)
admin.site.register(TeachingMethodHasPedagogicTactic)

admin.site.register(NavigationStyle)
admin.site.register(PedagogicStrategyGeneralRecommendation)

admin.site.register(LearningResource)
admin.site.register(PedagogicTacticHasLearningResource)

admin.site.register(PedagogicStrategySpecificRecommendation)
admin.site.register(Test)
admin.site.register(StyleName)
admin.site.register(LessonStructure)
admin.site.register(Structure)
admin.site.register(GivesSupportTo)
admin.site.register(Session)
admin.site.register(StructureHasStyleName)