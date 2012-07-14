# -*- coding: utf-8 -*
from django.contrib import admin
from cms.models import *

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('display', 'slug', 'url', 'type', 'public')
	search_fields = ('display', 'slug', 'url', 'type', 'public')
	list_filter = ('type', 'public')
	list_editable = ('public',)
	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

admin.site.register(Category, CategoryAdmin)
		
class PageAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['category']
	list_editable = ['order', 'public', 'main']
	class Media:
		js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

admin.site.register(Page, PageAdmin)