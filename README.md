# django-cms
Pages and categories for django.

# Install
* Add ```'cms',``` to ```INSTALLED_APPS ```
* Add ```'cms.middleware.PageMiddleware',``` to end of ```MIDDLEWARE_CLASSES```
* Add ```url(r'^', include('cms.urls')),``` to end of urls.py 
* manage.py syncdb
## Notise
If you want to use multilanguage you must instal ```django-modeltranslation```, define LANGUAGES in settings and use 'middleware.SwitchLocaleMiddleware', to change languages.


# To Do
* New templates
* Custom templates

* New views
* New **news** urls
	/news/some-thing-heppen/
	/news/page-1/
		http://ux.stackexchange.com/questions/16045/pagination-urls
		http://www.ayima.com/seo-knowledge/conquering-pagination-guide.html
	/news/2013/
	/news/2013/01/
	/news/2013/01/23/
* Optimize category models tree

# Change Log
## 2014.01.04
### Fix
* Change ```type``` to ```template```
* Change translation module
* Add slash checking (https://docs.djangoproject.com/en/dev/ref/settings/#append-slash)

## 2013.06.13
### Fix
* Optimization views.py
* Optimization templates
* New news templates

## 2012.11.07
### Add
* Templates for multilanguage
* DE Locale
### Fix
* views template puth
* README.md

## 2012.11.07
### Add
* Multilanguage
### Fix
* view()
* views::page() Optimization

## 2012.10.17
### Fix
* PEP-8
* Remove tiny_mce

## 2012.07.24
### Add
* Filter by sites.
* cms_render template tag

## 2012.07.14
### Add
* SafeUnicode to Category.
* Rename Pages to Page.
* Ordering to pages.

### Fix
* Optimized README.md
* Add permalink to get_absolute_url for Category.
* Optimized urls.py.
* Optimized Meta class of Category.
* Optimized url_puth method of Category.
* Optimized middleware PageMiddleware.
* Fix save method of Category. If you save category all childs will by saved and all pages of this category to change url.


## 2012.07.13
### Add
* Add get_absolute_url to Category.

### Fix
* Now, SEO is a standalone application.
* MetaTeg moved to SEO.
* Optimized middleware.
* Optimized Pages save method.
* Now use ugettext_lazy.

## 2012.07.11
### Add
* created_at
* updated_at

### Fix
* new README.md
* full_url field changed to url
* Optimized save method.
* Optimized url_puth method.
* Optimized display method.
* Optimized __unicode__ method.
