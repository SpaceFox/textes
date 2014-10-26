# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0002_auto_20141026_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='sequence',
            field=models.FloatField(default=1.0, verbose_name='Sequence'),
            preserve_default=True,
        ),
    ]
