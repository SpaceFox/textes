from django.shortcuts import render, get_object_or_404

from models import Chapter, ShortStory, Novel


def short_story(request, slug):

    text = get_object_or_404(ShortStory, slug=slug)
    short_stories = ShortStory.objects.all()
    novels = Novel.objects.all()
    licence = {
        u'title': text.title,
        u'url': text.get_absolute_url()
    }

    return render(request, u'literature/short_story.html', {
        u'text': text,
        u'licence': licence,
        u'short_stories': short_stories,
        u'novels': novels,
    })


def chapter(request, slug_novel, slug_chapter):

    text = get_object_or_404(Chapter, slug=slug_chapter)
    licence = {
        u'title': text.novel.title,
        u'url': text.novel.get_absolute_url()
    }

    return render(request, u'literature/chapter.html', {
        u'text': text,
        u'licence': licence,
    })


def novel(request, slug):
    novel = get_object_or_404(Novel, slug=slug)
    licence = {
        u'title': novel.title,
        u'url': novel.get_absolute_url()
    }
    return render(request, u'literature/novel.html', {
        u'novel': novel,
        u'licence': licence,
    })