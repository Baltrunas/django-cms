from django.conf.urls import url
from .views import category


urlpatterns = [
	url(r'^(?P<url>[-\D\w/_]+)/(?P<page>\d+)/$', category, name='cms_category_page'),
	url(r'^(?P<url>[-\D\w/_]+)/$', category, name='cms_category'),
]
