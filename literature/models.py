# coding: utf-8

from django.db import models
import markdown
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Genre(models.Model):

    """Genre of text"""

    name = models.CharField(u'Nom', max_length=50)
    slug = models.SlugField(u'Slug', unique=True, editable=False)
    description = models.TextField(u'Description')

    def save(self):
        self.slug = slugify(self.name)
        super(Genre, self).save()

    def __unicode__(self):
        return self.name


class Text(models.Model):

    """A text element (short story or chapter)"""

    title = models.CharField(u'Titre', max_length=50)
    slug = models.SlugField(u'Slug', unique=True, editable=False)
    text = models.TextField(u'Texte')
    text_html = models.TextField(u'Texte (HTML)', blank=True, editable=False)
    pub_date = models.DateTimeField(u'Date de publication', auto_now_add=True)
    last_update = models.DateTimeField(u'Date de dernière mise à jour', auto_now=True)
    author_comment = models.TextField(u'Commentaire de l\'auteur', null=True, blank=True)
    author_comment_html = models.TextField(u'Commentaire de l\'auteur (HTML)', null=True, blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        self.text_html = markdown.markdown(self.text)
        self.author_comment_html = markdown.markdown(self.author_comment)
        super(Text, self).save()

    class Meta:
        abstract = True


class ShortStory(Text):

    """A short story containing a single text"""

    genre = models.ManyToManyField(Genre, null=True, blank=True)

    def get_absolute_url(self):
        return reverse(u'literature.views.short_story', kwargs={u'slug': self.slug})

    def __unicode__(self):
        return u'{} (Nouvelle)'.format(self.title)

    class Meta:
        verbose_name = u'Nouvelle'


class Chapter(Text):

    """A novel chapter"""
    novel = models.ForeignKey(u'Novel')

    def get_absolute_url(self):
        return reverse(u'literature.views.chapter', kwargs={u'slug_chapter': self.slug, u'slug_novel': self.novel.slug})

    def __unicode__(self):
        return u'{} - {} (Roman)'.format(self.novel.title, self.title)

    class Meta:
        verbose_name = u'Chapitre'


class Novel(models.Model):

    """A novel contains several chapters"""

    title = models.CharField(u'Titre', max_length=50)
    slug = models.SlugField(u'Slug', unique=True, editable=False)
    genre = models.ManyToManyField(Genre, null=True, blank=True)
    pub_date = models.DateTimeField(u'Date de publication', auto_now_add=True)
    last_update = models.DateTimeField(u'Date de dernière mise à jour', auto_now=True)
    author_comment = models.TextField(u'Commentaire de l\'auteur', null=True, blank=True)
    author_comment_html = models.TextField(u'Commentaire de l\'auteur (HTML)', null=True, blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        self.author_comment_html = markdown.markdown(self.author_comment)
        super(Novel, self).save()

    def get_absolute_url(self):
        return reverse(u'literature.views.novel', kwargs={u'slug': self.slug})

    def __unicode__(self):
        return u'{} (Roman)'.format(self.title)

    class Meta:
        verbose_name = u'Roman'