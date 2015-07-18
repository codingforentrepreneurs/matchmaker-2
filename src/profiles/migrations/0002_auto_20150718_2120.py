# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(null=True, upload_to=profiles.models.upload_location, blank=True),
        ),
    ]
