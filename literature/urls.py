# coding: utf-8
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from models import ShortStory, Novel, Chapter


# SiteMap data
sitemaps = {
    'short_stories': GenericSitemap(
        {'queryset': ShortStory.objects.all(), 'date_field': 'last_update'},
        changefreq='daily',
        priority=0.7
    ),
    'novels': GenericSitemap(
        {'queryset': Novel.objects.all(), 'date_field': 'last_update'},
        changefreq='weekly',
        priority=0.7
    ),
    'chapters': GenericSitemap(
        {'queryset': Chapter.objects.all(), 'date_field': 'last_update'},
        changefreq='daily',
        priority=0.5
    ),
}

urlpatterns = patterns(
    '',
    url(r'^$', u'literature.views.home'),
    url(ur'^roman/(?P<slug_novel>.+)/(?P<slug_chapter>.+)/$', u'literature.views.chapter'),
    url(ur'^roman/(?P<slug>.+)/$', u'literature.views.novel'),
    url(ur'^nouvelle/(?P<slug>.+)/$', u'literature.views.short_story'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
