# -*- coding: utf-8 -*
from django.conf import settings
from django.contrib import admin
from cms.models import Category
from cms.models import Page


if 'hvad' in settings.INSTALLED_APPS and hasattr(settings, 'LANGUAGES'):
	from hvad.admin import TranslatableAdmin
	BaseAdminModel = TranslatableAdmin
else:
	BaseAdminModel = admin.ModelAdmin


class CategoryAdmin(BaseAdminModel):
	list_display = ['display', 'slug', 'url', 'type', 'public']
	search_fields = ['display', 'slug', 'url', 'type', 'public']
	list_filter = ['type', 'public', 'sites']
	list_editable = ['public']

admin.site.register(Category, CategoryAdmin)


class PageAdmin(BaseAdminModel):
	list_display = ['__unicode__', 'slug', 'url', 'order', 'public', 'main']
	search_fields = ['title', 'slug', 'url', 'public', 'text']
	list_filter = ['public', 'main', 'category', 'sites']
	list_editable = ['order', 'public', 'main']

admin.site.register(Page, PageAdmin)
