# -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url

urlpatterns = patterns('cms.views',
	#	news/id100/
	url(r'^(?P<url>\w+)/id(?P<id>\d+)/$', 'news_detail', name='cms_news_detail'),
	#	news/2000/
	url(r'^(?P<url>[-\w]+)/(?P<year>\d{4})/$', 'news_year_archive', name='cms_news_year_archive'),
	#	news/2000/04/
	url(r'^(?P<url>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/$', 'news_month_archive', name='cms_news_month_archive'),
	#	news/2000/04/30/
	url(r'^(?P<url>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'news_day_archive', name='cms_news_day_archive'),
	#	article/3/	-	article page 3
	url(r'^(?P<url>[-\D\w/_]+)/(?P<page>\d+)/$', 'category', name='cms_category_page'),
	#	article/
	url(r'^(?P<url>[-\D\w/_]+)/$', 'category', name='cms_category' ),
)
