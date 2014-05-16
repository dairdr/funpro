# -*- encoding: utf-8 -*-
"""Defines all views using Class Base Views."""
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.base import TemplateView
from django.views.generic.base import View