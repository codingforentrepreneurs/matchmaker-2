# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_employer_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='flagged',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='flagged',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
