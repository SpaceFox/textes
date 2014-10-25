# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, editable=False)),
                ('text', models.TextField(verbose_name='Texte')),
                ('text_html', models.TextField(verbose_name='Texte (HTML)', editable=False, blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Date de derni\xe8re mise \xe0 jour')),
                ('author_comment', models.TextField(null=True, verbose_name='Pr\xe9face', blank=True)),
                ('author_comment_html', models.TextField(verbose_name='Pr\xe9face (HTML)', null=True, editable=False, blank=True)),
                ('novel', models.ForeignKey(to='literature.Chapter')),
            ],
            options={
                'verbose_name': 'Chapitre',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, editable=False)),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, editable=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Date de derni\xe8re mise \xe0 jour')),
                ('author_comment', models.TextField(null=True, verbose_name='Pr\xe9face', blank=True)),
                ('author_comment_html', models.TextField(verbose_name='Pr\xe9face (HTML)', null=True, editable=False, blank=True)),
                ('genre', models.ManyToManyField(to='literature.Genre', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Roman',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShortStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('slug', models.SlugField(verbose_name='Slug', unique=True, editable=False)),
                ('text', models.TextField(verbose_name='Texte')),
                ('text_html', models.TextField(verbose_name='Texte (HTML)', editable=False, blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Date de derni\xe8re mise \xe0 jour')),
                ('author_comment', models.TextField(null=True, verbose_name='Pr\xe9face', blank=True)),
                ('author_comment_html', models.TextField(verbose_name='Pr\xe9face (HTML)', null=True, editable=False, blank=True)),
                ('genre', models.ManyToManyField(to='literature.Genre', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Nouvelle',
            },
            bases=(models.Model,),
        ),
    ]
