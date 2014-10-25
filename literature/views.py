from django.shortcuts import render, get_object_or_404

from models import Chapter, ShortStory


def short_story(request, slug):
    return render(request, u'literature/short_story.html', {
        u'text': get_object_or_404(ShortStory, slug=slug)
    })

def chapter(request, slug):
    return render(request, u'literature/chapter.html', {
        u'text': get_object_or_404(Chapter, slug=slug)
    })