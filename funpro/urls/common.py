# -*- coding: utf-8 -*-
"""Common urls."""
from django.contrib import admin
from django.conf.urls import patterns, include, url
from apps.account import urls as account_urls
from apps.dashboard import urls as dashboard_urls

# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Apps
	url(r'^account/', include(account_urls)),
	url(r'^dashboard/', include(dashboard_urls)),
)