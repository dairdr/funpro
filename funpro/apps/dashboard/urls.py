# -*- encoding: utf-8 -*-
"""Defines all urls conf."""
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import IndexView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='dashboard'),
)