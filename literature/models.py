# coding: utf-8

from django.db import models
import markdown

# Create your models here.


class Element(models.Model):

    """A text element"""

    title = models.CharField(u'Titre', max_length=50)
    slug = models.SlugField(u'Slug', unique=True)
    pub_date = models.DateTimeField(u'Date de publication', auto_now_add=True)
    last_update = models.DateTimeField(u'Date de dernière mise à jour', auto_now=True)
    preface = models.TextField(u'Préface', null=True, blank=True)
    preface_html = models.TextField(u'Préface (HTML)', null=True, blank=True)
    postface = models.TextField(u'Postface', null=True, blank=True)
    postface_html = models.TextField(u'Postface (HTML)', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.preface_html = markdown.markdown(self.preface)
        self.postface_html = markdown.markdown(self.postface)
        super(Element, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Book(Element):

    """A book, with one or more chapters"""

    def __unicode__(self):
        return self.title


class Chapter(Element):

    """A chapter or a single text"""

    book = models.ForeignKey(u'Book')
    text = models.TextField(u'Texte')
    text_html = models.TextField(u'Texte (HTML)', blank=True)

    def save(self, *args, **kwargs):
        self.text_html = markdown.markdown(self.text)
        super(Chapter, self).save(*args, **kwargs)