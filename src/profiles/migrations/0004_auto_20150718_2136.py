# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userjob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userjob',
            old_name='postion',
            new_name='position',
        ),
    ]
