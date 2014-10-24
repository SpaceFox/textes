# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Date de derni\xe8re mise \xe0 jour')),
                ('preface', models.TextField(null=True, verbose_name='Pr\xe9face', blank=True)),
                ('preface_html', models.TextField(null=True, verbose_name='Pr\xe9face (HTML)', blank=True)),
                ('postface', models.TextField(null=True, verbose_name='Postface', blank=True)),
                ('postface_html', models.TextField(null=True, verbose_name='Postface (HTML)', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de publication')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Date de derni\xe8re mise \xe0 jour')),
                ('preface', models.TextField(null=True, verbose_name='Pr\xe9face', blank=True)),
                ('preface_html', models.TextField(null=True, verbose_name='Pr\xe9face (HTML)', blank=True)),
                ('postface', models.TextField(null=True, verbose_name='Postface', blank=True)),
                ('postface_html', models.TextField(null=True, verbose_name='Postface (HTML)', blank=True)),
                ('text', models.TextField(verbose_name='Texte')),
                ('text_html', models.TextField(verbose_name='Texte (HTML)')),
                ('book', models.ForeignKey(to='literature.Book')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
