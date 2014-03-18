# -*- coding: utf-8 -*
from django.contrib import admin

from cms.models import Category
from cms.models import Page


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'slug', 'url', 'template', 'public']
	search_fields = ['__unicode__', 'slug', 'url', 'template', 'public']
	list_filter = ['template', 'public', 'sites']
	list_editable = ['public']

admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['public', 'main', 'category', 'sites']
	list_editable = ['order', 'public', 'main']

admin.site.register(Page, PageAdmin)
