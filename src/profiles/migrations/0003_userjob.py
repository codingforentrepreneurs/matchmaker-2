# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20150718_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postion', models.CharField(max_length=220)),
                ('location', models.CharField(max_length=220)),
                ('employer_name', models.CharField(max_length=220)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
