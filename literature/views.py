from django.shortcuts import render, get_object_or_404

from models import Chapter, ShortStory, Novel


def short_story(request, slug):

    text = get_object_or_404(ShortStory, slug=slug)
    licence = {
        u'title': text.title,
        u'url': text.get_absolute_url()
    }

    return render(request, u'literature/short_story.html', {
        u'text': text,
        u'licence': licence,
        u'short_stories': ShortStory.objects.all(),
        u'novels': Novel.objects.all(),
    })


def chapter(request, slug_novel, slug_chapter):

    text = get_object_or_404(Chapter, slug=slug_chapter)
    chapters = text.novel.chapter_set.all().order_by(u'sequence')
    previous_chapter = Chapter.objects.filter(sequence__lt=text.sequence).order_by(u'-sequence').first()
    next_chapter = Chapter.objects.filter(sequence__gt=text.sequence).order_by(u'sequence').first()

    licence = {
        u'title': text.novel.title,
        u'url': text.novel.get_absolute_url()
    }

    return render(request, u'literature/chapter.html', {
        u'text': text,
        u'licence': licence,
        u'chapters': chapters,
        u'short_stories': ShortStory.objects.all(),
        u'novels': Novel.objects.all(),
        u'previous_chapter': previous_chapter,
        u'next_chapter': next_chapter,
    })


def novel(request, slug):

    novel = get_object_or_404(Novel, slug=slug)
    chapters = novel.chapter_set.all().order_by(u'sequence')
    licence = {
        u'title': novel.title,
        u'url': novel.get_absolute_url()
    }
    return render(request, u'literature/novel.html', {
        u'novel': novel,
        u'licence': licence,
        u'chapters': chapters,
        u'short_stories': ShortStory.objects.all(),
        u'novels': Novel.objects.all(),
    })
