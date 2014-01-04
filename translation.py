# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from cms.models import Category
from cms.models import Page

class CategoryTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(Category, CategoryTranslationOptions)


class PageTranslationOptions(TranslationOptions):
	fields = ['title', 'header', 'keywords', 'description', 'intro_text', 'text']

translator.register(Page, PageTranslationOptions)
