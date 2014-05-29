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

from models import Test

class IndexView(TemplateView):
	"""Represents index page."""
	http_method_names = ['get']
	template_name = 'dashboard/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
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
	http_method_names = ['post','get']
	redirect_url = 'dashboard-profile'

	def post(self, request):
		g1 = check_answers(ACT_REF, request, ['activo','reflexivo'])
		g2 = check_answers(SEN_INT, request, ['sensorial','intuitivo'])
		g3 = check_answers(VIS_VRB, request, ['visual','verbal'])
		g4 = check_answers(SEC_GLO, request, ['secuencial','global'])
		messages.success(request, 'Resultados: %s, %s, %s, %s' % (g1, g2, g3, g4))
		return HttpResponseRedirect(reverse(self.redirect_url))