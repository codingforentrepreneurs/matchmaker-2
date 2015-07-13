# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0004_auto_20150713_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('my_answer_importance', models.CharField(max_length=50, choices=[(b'Mandatory', b'Mandatory'), (b'Very Important', b'Very Important'), (b'Somewhat Important', b'Somewhat Important'), (b'Not Important', b'Not Important')])),
                ('their_importance', models.CharField(max_length=50, choices=[(b'Mandatory', b'Mandatory'), (b'Very Important', b'Very Important'), (b'Somewhat Important', b'Somewhat Important'), (b'Not Important', b'Not Important')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(related_name='user_answer', to='questions.Answer')),
                ('question', models.ForeignKey(to='questions.Question')),
                ('their_answer', models.ForeignKey(related_name='match_answer', blank=True, to='questions.Answer', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
