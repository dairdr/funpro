# -*- encoding: utf-8 -*-
"""Defines all views using Class Base Views."""
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.db import transaction, IntegrityError
from libs.utils.utils import check_answers, ACT_REF, SEN_INT, VIS_VRB, SEC_GLO
from django.contrib import messages

from models import *

class IndexView(TemplateView):
	"""Represents index page."""
	http_method_names = ['get']
	template_name = 'dashboard/courses.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		try:
			learning_style_dimension = LearningStyleDimension.objects.get(student=self.request.user)
			pedagogical_strategy_context = PedagogicalStrategyContext.objects.get(learning_style_dimension=learning_style_dimension)
			general_recommendation = PedagogicStrategyGeneralRecommendation.objects.filter(pedagogical_strategy_context=pedagogical_strategy_context)
			specific_recommendation = PedagogicStrategySpecificRecommendation.objects.filter(pedagogic_strategy_general_recommendation=general_recommendation)
		except:
			pass
		else:
			Session.objects.filter()

		try:
			courses = StudentHasCourse.objects.filter(student=self.request.user)
		except:
			pass
		else:
			context.update({'courses':courses})
		return context

class ProfileView(TemplateView):
	"""Represents profile page."""
	http_method_names = ['get']
	template_name = 'dashboard/profile.html'

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		return context

class TestView(TemplateView):
	"""Represents felder test page."""
	http_method_names = ['get']
	template_name = 'dashboard/test.html'

	def get_context_data(self, **kwargs):
		context = super(TestView, self).get_context_data(**kwargs)
		context.update({'test':Test.objects.all()})
		return context

class SaveTestView(View):
	"""Save felder test."""
	http_method_names = ['post']
	redirect_url = 'dashboard-profile'

	def post(self, request):
		try:
			style_names = StyleName.objects.all()
		except:
			pass
		else:
			g1 = check_answers(ACT_REF, request, [style_names[0],style_names[1]])
			g2 = check_answers(SEN_INT, request, [style_names[2],style_names[3]])
			g3 = check_answers(VIS_VRB, request, [style_names[4],style_names[5]])
			g4 = check_answers(SEC_GLO, request, [style_names[6],style_names[7]])
			messages.success(request, 'Resultados: %s, %s, %s, %s' % (g1, g2, g3, g4))

			try:
				with transaction.atomic():
					learning_style, created = LearningStyle.objects.get_or_create(processing=g1, perception=g2, reception=g3, understanding=g4)
					learning_style_dimension, created = LearningStyleDimension.objects.get(student=request.user, learning_style=learning_style)
			except:
				pass
		return HttpResponseRedirect(reverse(self.redirect_url))

class CourseView(TemplateView):
	"""Represents course."""
	http_method_names = ['get']
	template_name = 'dashboard/courses.html'

	def get_context_data(self, **kwargs):
		context = super(CourseView, self).get_context_data(**kwargs)
		return context