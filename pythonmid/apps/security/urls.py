__author__ = 'alex'
from django.conf.urls import patterns, url


urlpatterns = patterns('pythonmid.apps.security.views',
                       url(r'^$', 'index_view', name="index"),
                       url(r'^logout/$', 'logout_view', name="logout"),
                       )