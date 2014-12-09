from modeltranslation.translator import translator, TranslationOptions

from .models import Category
from .models import Page


class CategoryTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(Category, CategoryTranslationOptions)


class PageTranslationOptions(TranslationOptions):
	fields = ['title', 'header', 'keywords', 'description', 'intro_text', 'text']

translator.register(Page, PageTranslationOptions)
