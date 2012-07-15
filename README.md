# django-cms
Pages and categories for django.

# Install
* Add 'cms', to INSTALLED_APPS
* Add to MIDDLEWARE_CLASSES 'cms.middleware.Redirect','cms.middleware.PageMiddleware',
* Add 	url(r'^', include('cms.urls')), to urls.py
* manage syncdb

# Futures
* Templates paganation
* New views
* New templates

# I think about
* tree to category parent select

# Changelog
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
