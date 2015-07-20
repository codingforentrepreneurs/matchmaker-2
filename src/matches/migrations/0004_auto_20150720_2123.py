# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0004_auto_20150720_2013'),
        ('matches', '0003_auto_20150720_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(to='jobs.Job')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobmatch',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobmatch',
            name='user',
        ),
        migrations.DeleteModel(
            name='JobMatch',
        ),
    ]
