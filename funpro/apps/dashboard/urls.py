# -*- encoding: utf-8 -*-
"""Defines all urls conf."""
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import IndexView, ProfileView, TestView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='dashboard'),
	url(r'^profile/$', ProfileView.as_view(), name='dashboard-profile'),
	url(r'^test/$', TestView.as_view(), name='dashboard-test'),
)