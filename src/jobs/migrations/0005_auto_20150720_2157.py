# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20150720_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
    ]
