# -*- encoding: utf-8 -*-
"""Defines all views using Class Base Views."""
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView
from django.views.generic.base import View

from models import Test

class IndexView(TemplateView):
	"""Represents index page."""
	http_method_names = ['get']
	template_name = 'dashboard/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		return context

class ProfileView(TemplateView):
	"""Represents index page."""
	http_method_names = ['get']
	template_name = 'dashboard/profile.html'

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		return context

class TestView(TemplateView):
	"""Represents index page."""
	http_method_names = ['get']
	template_name = 'dashboard/test.html'

	def get_context_data(self, **kwargs):
		context = super(TestView, self).get_context_data(**kwargs)
		context.update({'test':Test.objects.all()})
		return context