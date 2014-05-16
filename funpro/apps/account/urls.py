# -*- encoding: utf-8 -*-
"""Defines all urls conf."""
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	url(r'^login/$', login, { 'template_name':'account/login.html' }, name='account-login'),
	url(r'^logout/$', logout, { 'template_name':'account/logout.html' }, name='account-logout'),
)