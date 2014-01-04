# -*- coding: utf-8 -*
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from cms.models import Category
from cms.models import Page


class CategoryAdmin(TranslationAdmin):
	list_display = ['__unicode__', 'slug', 'url', 'template', 'public']
	search_fields = ['__unicode__', 'slug', 'url', 'template', 'public']
	list_filter = ['template', 'public', 'sites']
	list_editable = ['public']

	class Media:
		js = (
			'//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}

admin.site.register(Category, CategoryAdmin)


class PageAdmin(TranslationAdmin):
	list_display = ['__unicode__', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['public', 'main', 'category', 'sites']
	list_editable = ['order', 'public', 'main']

	class Media:
		js = (
			'//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}

admin.site.register(Page, PageAdmin)
