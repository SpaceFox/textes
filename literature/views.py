from django.shortcuts import render, get_object_or_404

from models import Chapter


def chapter(request, slug):
    return render(request, u'literature/chapter.html', {
        u'chapter': get_object_or_404(Chapter, slug=slug)
    })
