# -*- coding: utf-8 -*
from django.db import models

from django.utils.safestring import SafeUnicode

from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
	
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
	type = models.CharField(verbose_name=_('Type'), max_length=16, choices=TYPE_CHOICES)
	
	text = models.TextField(
		verbose_name=_('Text'),
		help_text=_('''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">ON \ OFF</a>'''),
		blank=True,
		null=True
	)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def url_puth (self, this):
		if this.parent:
			return self.url_puth(this.parent) + '/' + this.slug
		else:
			return this.slug

	def save(self, *args, **kwargs):
		self.url = self.url_puth(self)
		super(Category, self).save(*args, **kwargs)
		for child in self.childs.all():
			child.save()
		for page in self.pages.all():
			page.save()

	def display(self):
		return '&nbsp;' * (len(self.url.split('/')) -1) * 6 + self.name
	display.short_description = _('Category')
	display.allow_tags = True

	@models.permalink
	def get_absolute_url(self):
		return ('cms_category', (), {'url': self.url})

	def __unicode__(self):
		return SafeUnicode('&nbsp;' * (len(self.url.split('/')) -1) * 6 + self.name)

	class Meta:
		ordering = ['url']
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')

class Page(models.Model):
	title = models.CharField(verbose_name=_('Title'), max_length=256)
	header = models.CharField(verbose_name=_('Header'), max_length=256)
	keywords = models.CharField(verbose_name=_('Keywords'), max_length=1024, blank=True, null=True)
	description = models.CharField(verbose_name=_('Description'), max_length=2048, blank=True, null=True)
	slug = models.CharField(verbose_name=_('Slug'), max_length=256, default='#')
	url = models.CharField(verbose_name=_('URL'), max_length=1024, editable=False)
	category = models.ForeignKey(Category, verbose_name=_('Categories'), related_name='pages', blank=True, null=True)
	intro_text = models.TextField(
		verbose_name=_('Intro Text'),
		help_text=_('''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_intro_text');">ON \ OFF</a>'''),
		blank=True,
		null=True
	)
	text = models.TextField(
		verbose_name=_('Text'),
		help_text=_('''<a class="btn" href="#" onclick="tinyMCE.execCommand('mceToggleEditor', false, 'id_text');">ON \ OFF</a>'''),
		blank=True,
		null=True
	)
	order = models.IntegerField(verbose_name=_('Order'), default=500, blank=True, null=True)
	img = models.FileField(verbose_name=_('Image'), upload_to='img/pages', blank=True)
	sites = models.ManyToManyField(Site, related_name='pages', verbose_name=_('Sites'), null=True, blank=True)
	
	views = models.PositiveIntegerField(verbose_name=_('Views'), editable=False, default=0)
	
	main = models.BooleanField(verbose_name=_('Main'))
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def save(self, *args, **kwargs):
		if self.category and self.category.type in ['blog', 'article']:
			self.url = '/' + self.category.url + '/' + self.slug + '/'
		else :
			self.url = '/' + self.slug
		super(Page, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return self.url

	class Meta:
		ordering = ['url']
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')
