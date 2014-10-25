from django.contrib import admin

from .models import Genre, ShortStory, Chapter, Novel


admin.site.register(Genre)
admin.site.register(ShortStory)
admin.site.register(Chapter)
admin.site.register(Novel)