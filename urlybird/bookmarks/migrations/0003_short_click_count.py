# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20151016_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='short',
            name='click_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
