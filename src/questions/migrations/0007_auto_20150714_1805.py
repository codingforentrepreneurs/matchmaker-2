# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20150714_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='active',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='my_points',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='their_points',
        ),
    ]
