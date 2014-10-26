# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='author_comment',
            field=models.TextField(null=True, verbose_name="Commentaire de l'auteur", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='author_comment_html',
            field=models.TextField(verbose_name="Commentaire de l'auteur (HTML)", null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='novel',
            field=models.ForeignKey(to='literature.Novel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='novel',
            name='author_comment',
            field=models.TextField(null=True, verbose_name="Commentaire de l'auteur", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='novel',
            name='author_comment_html',
            field=models.TextField(verbose_name="Commentaire de l'auteur (HTML)", null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shortstory',
            name='author_comment',
            field=models.TextField(null=True, verbose_name="Commentaire de l'auteur", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shortstory',
            name='author_comment_html',
            field=models.TextField(verbose_name="Commentaire de l'auteur (HTML)", null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
