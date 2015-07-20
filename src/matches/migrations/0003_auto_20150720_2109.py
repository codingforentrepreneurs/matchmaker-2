# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_employermatch_jobmatch_locationmatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employermatch',
            name='liked',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='jobmatch',
            name='liked',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='locationmatch',
            name='liked',
            field=models.NullBooleanField(),
        ),
    ]
