# -*- encoding: utf-8 -*-
"""Defines all urls conf."""
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import IndexView, ProfileView, TestView, SaveTestView

urlpatterns = patterns('',
	url(r'^$', login_required(IndexView.as_view()), name='dashboard'),
	url(r'^profile/$', login_required(ProfileView.as_view()), name='dashboard-profile'),
	url(r'^test/$', login_required(TestView.as_view()), name='dashboard-test'),
	url(r'^test/save/$', login_required(SaveTestView.as_view()), name='dashboard-save-test'),
)