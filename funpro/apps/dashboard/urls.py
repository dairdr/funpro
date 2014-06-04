# -*- encoding: utf-8 -*-
"""Defines all urls conf."""
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import IndexView, ProfileView, TestView, SaveTestView, CourseView

urlpatterns = patterns('',
	url(r'^$', login_required(IndexView.as_view()), name='dashboard'),
	url(r'^profile/$', login_required(ProfileView.as_view()), name='dashboard-profile'),
	url(r'^test/$', login_required(TestView.as_view()), name='dashboard-test'),
	url(r'^test/save/$', login_required(SaveTestView.as_view()), name='dashboard-save-test'),
	url(r'^(?P<course>\w{5,45})/$', login_required(CourseView.as_view()), name='dashboard-course'),
)