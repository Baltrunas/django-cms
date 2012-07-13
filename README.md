# django-cms
Pages and categories for django.

# Install
1) Add 'cms', to INSTALLED_APPS
2) Add to MIDDLEWARE_CLASSES 'cms.middleware.Redirect', 'cms.middleware.PageMiddleware',
3) Add 	url(r'^', include('cms.urls')), to urls.py
4) manage syncdb
5) TEMPLATE_CONTEXT_PROCESSORS 	'cms.middleware.SEO',

# Futures
* tree to category parent select

# Changelog
## 2012.07.13
* Now, SEO is a standalone application.
* Optimized middleware.

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

