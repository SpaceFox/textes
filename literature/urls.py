# coding: utf-8
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(ur'^roman/(?P<slug_novel>.+)/(?P<slug_chapter>.+)/$', u'literature.views.chapter'),
    url(ur'^roman/(?P<slug>.+)/$', u'literature.views.novel'),
    url(ur'^nouvelle/(?P<slug>.+)/$', u'literature.views.short_story'),
)
if settings.DEBUG:
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
