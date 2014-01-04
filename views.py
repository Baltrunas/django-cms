# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator

from cms.models import Page
from cms.models import Category


def page(request, url):
	context = {}
	host = request.META.get('HTTP_HOST')
	page = get_object_or_404(Page, url=url, sites__domain__in=[host])
	page.view()
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description

	if page.category:
		template = 'cms/' + page.category.type + '_detail.html'
	else:
		template = 'cms/page_detail.html'

	return render_to_response(template, context, context_instance=RequestContext(request))


def category(request, url, page=1):
	context = {}
	host = request.META.get('HTTP_HOST')
	category = get_object_or_404(Category, url=url, sites__domain__in=[host])
	context['category'] = category
	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name

	host = request.META.get('HTTP_HOST')
	# pages_list = Page.objects.filter(public=True, category=context['category'].id, sites__domain__in=[host]).order_by('-created_at')
	pages_list = Page.objects.filter(public=True, category__in=context['category'].all_sub(), sites__domain__in=[host]).order_by('-created_at')
	paginator = Paginator(pages_list, context['category'].per_page)

	try:
		pages_list = paginator.page(page)
	except:
		pages_list = paginator.page(1)

	context['pages_list'] = pages_list

	template = 'cms/%s_archive.html' % category.type

	return render_to_response(template, context, context_instance=RequestContext(request))
