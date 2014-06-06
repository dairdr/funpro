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
import logging

from models import *

class IndexView(TemplateView):
	"""Represents index page."""
	http_method_names = ['get']
	template_name = 'dashboard/courses.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		# logger = logging.getLogger(__name__)
		# logger.debug("this is a error message!")

		id_specific = 3
		id_new_resource = 4

		with transaction.atomic():
			# actualizar y castigar recomendacion actual.
			specific = PedagogicStrategySpecificRecommendation.objects.get(id=id_specific)

			# conseguir datos del nuevo recurso.
			resource = LearningResource.objects.get(id=id_new_resource)

			# extraer los id de las tacticas a las que pertenece al nuevo recurso.
			tactics = PedagogicTactic.objects.filter(learning_resource=resource).values_list('id')

			# current general
			current_general = specific.pedagogic_strategy_general_recommendation

			# current pedagogic tactic
			current_ped_tac = specific.pedagogic_tactic

			if not specific.pedagogic_tactic.id in tactics:
				# buscar los metodos de ensenanza a los que pertenece las tacticas pedagogicas.
				teaching_methods = TeachingMethod.objects.filter(pedagogic_tactic__id__in=tactics).values_list('id')
				tm = TeachingMethod.objects.filter(id__in=teaching_methods)

				if not specific.pedagogic_strategy_general_recommendation.teaching_method.id in teaching_methods:
					# castigo moderado
					specific.pedagogic_strategy_general_recommendation.performance -= 1

					index = 0
					ids = []
					while tm[index].learning_theory.id not specific.pedagogic_strategy_general_recommendation.learning_theory.id and (index < len(tm)):
						ids.append(tm[index].learning_theory.id)
						index += 1

					psgr = None
					if index < len(tm):
						psgr = PedagogicStrategyGeneralRecommendation(
							performance=0,
							pedagogic_tactic_context=None,# enviarlo por GUI
							teaching_method=tm[index],
							learning_theory=tm[index].learning_theory,
							status=True,
							generated='manual'
						)
					else:
						psgr = PedagogicStrategyGeneralRecommendation(
							performance=0,
							pedagogic_tactic_context=None,# enviarlo por GUI
							teaching_method=tm[0],
							learning_theory=tm[0].learning_theory,
							status=True,
							generated='manual'
						)
					current_general = psgr
					psgr.save()

					if specific.pedagogic_strategy_general_recommendation.learning_theory.id in ids:
						pass
					else:
						# castigo severo
						specific.pedagogic_strategy_general_recommendation.performance -= 1
				else:
					tactic_candidates = PedagogicTactic.objects.filter(teaching_method__id__in=teaching_methods).values_list('id')
					current_ped_tac = tactic_candidates[0]

			specific.status = False
			specific.performance -= 1
			specific.save()

			# insertar nuevo registro especifico
			pssr = PedagogicStrategySpecificRecommendation(
				performance=0,
				learning_resource=resource,
				pedagogic_strategy_general_recommendation=current_general,
				lesson_component=None,# enviarlo por GUI
				pedagogic_tactic=current_ped_tac,
				status=True,
				generated='manual'
			)
			pssr.save()

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