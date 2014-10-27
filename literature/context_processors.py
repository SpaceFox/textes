# coding: utf-8
from django.conf import settings
from models import ShortStory, Novel


def global_settings(request):
    return {
        u'short_stories': ShortStory.objects.all().order_by(u'-last_update'),
        u'novels': Novel.objects.all().order_by(u'-last_update'),
        u'GOOGLE_ANALYTICS': settings.GOOGLE_ANALYTICS,
    }