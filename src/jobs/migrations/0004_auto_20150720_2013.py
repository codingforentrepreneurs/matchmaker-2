# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150718_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.CharField(unique=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(unique=True, max_length=250),
        ),
    ]
