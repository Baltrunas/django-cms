# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.template import RequestContext

from datetime import datetime

from cms.models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

context = {}

def page(request, url):
	page = get_object_or_404(Page, url=url)
	page.views += 1
	page.save()
	context['url'] = url
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description
	if (page.category):
		if (page.category.type == 'article'):
			return render_to_response('article_detail.html', context, context_instance = RequestContext(request))
		elif (page.category.type == 'blog'):
			return render_to_response('blog_detail.html', context, context_instance = RequestContext(request))
		elif (page.category.type == 'news'):
			return render_to_response('news_detail.html', context, context_instance = RequestContext(request))
	return render_to_response('page_detail.html', context, context_instance = RequestContext(request))

def category(request, url, page=1):
	category = get_object_or_404(Category, url=url)
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
	article_archive = Page.objects.filter(public=True, category=context['category'].id).order_by('-created_at')
	paginator = Paginator(article_archive, 4)
	try:
		article_archive = paginator.page(page)
	except PageNotAnInteger:
		article_archive = paginator.page(1)
	except EmptyPage:
		article_archive = paginator.page(1)
	context['article_archive'] = article_archive
	return render_to_response('article_archive.html', context, context_instance = RequestContext(request))

def blog_archive(request, url, page=1):
	blog_archive = Page.objects.filter(public=True, category=context['category'].id).order_by('-created')
	paginator = Paginator(blog_archive, 1)
	try:
		blog_archive = paginator.page(page)
	except PageNotAnInteger:
		blog_archive = paginator.page(1)
	except EmptyPage:
		blog_archive = paginator.page(1)
	context['blog_archive'] = blog_archive
	return render_to_response('blog_archive.html', context, context_instance = RequestContext(request))

def news_archive(request, url):
	year = datetime.now().year
	category = get_object_or_404(Category, url=url)
	context['news_year'] = year
	context['category'] = category
	
	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_archive.html', context, context_instance = RequestContext(request))

def news_year_archive(request, url, year):
	category = get_object_or_404(Category, url=url)
	context['news_year'] = int(year)
	context['category'] = category
	
	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_year_archive.html', context, context_instance = RequestContext(request))

def news_month_archive(request, url, year, month):
	category = get_object_or_404(Category, url=url)
	context['news_year'] = int(year)
	context['news_month'] = int(month)
	context['category'] = category
	
	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year
	).order_by('-created_at')

	context['news_month_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		created_at__month=month
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_month_archive.html', context, context_instance = RequestContext(request))

def news_day_archive(request, url, year, month, day):
	category = get_object_or_404(Category, url=url)
	context['news_year'] = int(year)
	context['news_month'] = int(month)
	context['news_day'] = int(day)
	context['category'] = category
	
	context['news_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
	).order_by('-created_at')

	context['news_year_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year
	).order_by('-created_at')

	context['news_month_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		created_at__month=month
	).order_by('-created_at')

	context['news_day_archive'] = Page.objects.filter(
		public=True,
		category=category.id,
		created_at__year=year,
		created_at__month=month,
		created_at__day=day
	).order_by('-created_at')

	context['title'] = category.name
	context['header'] = category.name
	context['keywords'] = category.name
	context['description'] = category.name
	return render_to_response('news_day_archive.html', context, context_instance = RequestContext(request))

def news_detail(request, url, id):
	category = get_object_or_404(Category, url=url)
	page = get_object_or_404(Page, id=id, category=category.id)
	context['page'] = page
	context['title'] = page.title
	context['header'] = page.header
	context['keywords'] = page.keywords
	context['description'] = page.description
	return render_to_response('news_detail.html', context, context_instance = RequestContext(request))