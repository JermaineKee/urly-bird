# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='click',
            old_name='clicker_ID',
            new_name='clicker',
        ),
        migrations.RenameField(
            model_name='click',
            old_name='short_ID',
            new_name='short',
        ),
    ]
