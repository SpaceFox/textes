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
            name='text_html',
            field=models.TextField(verbose_name='Texte (HTML)', blank=True),
            preserve_default=True,
        ),
    ]
