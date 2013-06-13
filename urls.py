# -*- coding: utf-8 -*
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('cms.views',
	# article/3/ article page 3
	url(r'^(?P<url>[-\D\w/_]+)/(?P<page>\d+)/$', 'category', name='cms_category_page'),
	# article/
	url(r'^(?P<url>[-\D\w/_]+)/$', 'category', name='cms_category'),
)
