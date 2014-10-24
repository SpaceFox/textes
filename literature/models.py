# coding: utf-8

from django.db import models
import markdown
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.


class Element(models.Model):

    """A text element"""

    title = models.CharField(u'Titre', max_length=50)
    slug = models.SlugField(u'Slug', unique=True, editable=False)
    pub_date = models.DateTimeField(u'Date de publication', auto_now_add=True)
    last_update = models.DateTimeField(u'Date de dernière mise à jour', auto_now=True)
    preface = models.TextField(u'Préface', null=True, blank=True)
    preface_html = models.TextField(u'Préface (HTML)', null=True, blank=True, editable=False)
    postface = models.TextField(u'Postface', null=True, blank=True)
    postface_html = models.TextField(u'Postface (HTML)', null=True, blank=True, editable=False)

    def save(self):
        self.preface_html = markdown.markdown(self.preface)
        self.postface_html = markdown.markdown(self.postface)
        self.slug = slugify(self.title)
        super(Element, self).save()

    class Meta:
        abstract = True


class Book(Element):

    """A book, with one or more chapters"""

    def __unicode__(self):
        return u'Livre {}'.format(self.title)


class Chapter(Element):

    """A chapter or a single text"""

    book = models.ForeignKey(u'Book')
    text = models.TextField(u'Texte')
    text_html = models.TextField(u'Texte (HTML)', blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.text_html = markdown.markdown(self.text)
        super(Chapter, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'Chapitre {}'.format(self.title)

    def get_absolute_url(self):
        return reverse(u'literature.views.chapter', kwargs={u'slug': self.slug})
