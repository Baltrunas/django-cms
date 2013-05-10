# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from datetime import datetime
from cms.models import Page
from cms.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

context = {}


def page(request, url):
	host = request.META.get('HTTP_HOST')
	page = get_object_or_404(Page, url=url, sites__domain__in=[host])
	page.view()
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description
	if page.category:
		try:
			return render_to_response('cms/' + page.category.type + '_detail.html', context, context_instance=RequestContext(request))
		except:
			return render_to_response('cms/page_detail.html', context, context_instance=RequestContext(request))
	else:
		return render_to_response('cms/page_detail.html', context, context_instance=RequestContext(request))


def category(request, url, page=1):
	host = request.META.get('HTTP_HOST')
	category = get_object_or_404(Category, url=url, sites__domain__in=[host])
	context['category'] = category
	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	if (category.type == 'article'):
		return article_archive(request, url, page)
	elif (category.type == 'blog'):
		return blog_archive(request, url, page)
	elif (category.type == 'news'):
		return news_archive(request, url)


def article_archive(request, url, page=1):
	host = request.META.get('HTTP_HOST')
	article_archive = Page.objects.filter(public=True, category=context['category'].id, sites__domain__in=[host]).order_by('-created_at')
	paginator = Paginator(article_archive, context['category'].per_page)
	try:
		article_archive = paginator.page(page)
	except PageNotAnInteger:
		article_archive = paginator.page(1)
	except EmptyPage:
		article_archive = paginator.page(1)
	context['article_archive'] = article_archive
	return render_to_response('cms/article_archive.html', context, context_instance=RequestContext(request))


def blog_archive(request, url, page=1):
	host = request.META.get('HTTP_HOST')
	blog_archive = Page.objects.filter(public=True, category=context['category'].id, sites__domain__in=[host]).order_by('-created_at')
	paginator = Paginator(blog_archive, context['category'].per_page)
	try:
		blog_archive = paginator.page(page)
	except PageNotAnInteger:
		blog_archive = paginator.page(1)
	except EmptyPage:
		blog_archive = paginator.page(1)
	context['blog_archive'] = blog_archive
	return render_to_response('cms/blog_archive.html', context, context_instance=RequestContext(request))


def news_archive(request, url):
	host = request.META.get('HTTP_HOST')
	year = datetime.now().year
	category = get_object_or_404(Category, url=url, sites__domain__in=[host])
	context['news_year'] = year
	context['category'] = category

	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('cms/news_archive.html', context, context_instance=RequestContext(request))


def news_year_archive(request, url, year):
	host = request.META.get('HTTP_HOST')
	category = get_object_or_404(Category, url=url, sites__domain__in=[host])
	context['news_year'] = int(year)
	context['category'] = category

	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('cms/news_year_archive.html', context, context_instance=RequestContext(request))


def news_month_archive(request, url, year, month):
	host = request.META.get('HTTP_HOST')
	category = get_object_or_404(Category, url=url, sites__domain__in=[host])
	context['news_year'] = int(year)
	context['news_month'] = int(month)
	context['category'] = category

	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['news_month_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		created_at__month=month,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('cms/news_month_archive.html', context, context_instance=RequestContext(request))


def news_day_archive(request, url, year, month, day):
	host = request.META.get('HTTP_HOST')
	category = get_object_or_404(Category, url=url, sites__domain__in=[host])
	context['news_year'] = int(year)
	context['news_month'] = int(month)
	context['news_day'] = int(day)
	context['category'] = category

	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['news_month_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		created_at__month=month,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['news_day_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		created_at__month=month,
		created_at__day=day,
		sites__domain__in=[host]
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('cms/news_day_archive.html', context, context_instance=RequestContext(request))


def news_detail(request, url, id):
	host = request.META.get('HTTP_HOST')
	category = get_object_or_404(Category, url=url, sites__domain__in=[host])
	page = get_object_or_404(Page, id=id, category=category.id, sites__domain__in=[host])
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description
	return render_to_response('cms/news_detail.html', context, context_instance=RequestContext(request))
