# -*- coding: utf-8 -*
from django.db import models

from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _
	
class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	slug = models.SlugField(verbose_name=_('Slug'), unique=True)
	url = models.CharField(verbose_name=_('URL'), max_length=512, editable=False)
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')

	TYPE_CHOICES = (
		('article', _('Article')),
		('blog', _('Blog')),
		('news', _('News')),
	)
	type = models.CharField(verbose_name=_('Type'), max_length=10, choices=TYPE_CHOICES)
	
	text = models.TextField(
		verbose_name=_('Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">''' + _('ON \ OFF') + '</a> ' + _('Text'),
		blank=True
	)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def url_puth (self, this):
		url_puth = this.slug
		if this.parent:
			return self.url_puth(this.parent) + '/' + url_puth
		else:
			return url_puth

	def save(self, *args, **kwargs):
		self.url = self.url_puth(self)
		super(Category, self).save(*args, **kwargs)

	def display(self):
		return '&nbsp;' * (len(self.url.split('/')) -1) * 8 + self.name
	display.short_description = _('Menu')
	display.allow_tags = True

	def __unicode__(self):
		return '&nbsp;' * (len(self.url.split('/')) -1) * 8 + self.name
	__unicode__.short_description = _('Menu')
	__unicode__.allow_tags = True

	class Meta:
		ordering = ['url', 'name']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')

class Pages(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=512)
	description = models.CharField(verbose_name=_('Description'), max_length=512)

	url = models.CharField(verbose_name=_('URL'), max_length=256, default='#')
	full_url = models.CharField(verbose_name=_('Full URL'), max_length=512, editable=False)

	TYPE_CHOICES = (
		('page', _('Page')),
		('article', _('Article')),
		('blog', _('Blog')),
		('news', _('News')),
	)

	type = models.CharField(verbose_name=_('Type'), max_length=10, choices=TYPE_CHOICES)
	category = models.ForeignKey(Category, verbose_name=_('Categories'), blank=True, null=True, help_text=_('Archives, News and Blogs ONLY!'))

	intro_text = models.TextField(
		verbose_name=_('Intro Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_intro_text');">''' + _('ON \ OFF') + '</a> ' + _('Info'),
		blank=True,
		null=True
	)

	text = models.TextField(
		verbose_name=_('Text'),
		help_text='''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">''' + _('ON \ OFF') + '</a> ' + _('Info'),
		blank=True,
		null=True
	)

	img = models.FileField(verbose_name=_('Image'), upload_to='img/pages', blank=True)

	sites = models.ManyToManyField(Site, related_name='pages', verbose_name=_('Sites'), null=True, blank=True)
	
	views = models.PositiveIntegerField(verbose_name=_('Views'), editable=False, default=0)
	
	main = models.BooleanField(verbose_name=_('Main'), default=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	
	
	def save(self, *args, **kwargs):
		super(Pages, self).save(*args, **kwargs)
		if self.type == 'blog' or self.type == 'article':
			self.full_url = '/' + self.category.full_url + '/' + self.url + '/'
		else :
			self.full_url = self.url
		super(Pages, self).save(*args, **kwargs)

	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return self.full_url
		
	class Meta:
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')


class MetaTeg(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	value = models.CharField(verbose_name=_('Info'), max_length=2048, blank=True)
	TYPE_CHOICES = (
		('meta', _('Meta')),
		('script', _('Script')),
		('link', _('Link')),
	)
	type = models.CharField(verbose_name=_('Type'), max_length=64, choices=TYPE_CHOICES)
	pages = models.ForeignKey(Pages, verbose_name=_('Page'))

	def __unicode__(self):
		return self.name + ' = ' + self.value

	class Meta:
		ordering = ['name']
		verbose_name = _('Meta Teg')
		verbose_name_plural = _('Meta Tegs')