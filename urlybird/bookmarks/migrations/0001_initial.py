# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('clicker_ID', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Short',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('bookmark', models.URLField()),
                ('short_url', models.URLField()),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='click',
            name='short_ID',
            field=models.ForeignKey(to='bookmarks.Short'),
        ),
    ]
