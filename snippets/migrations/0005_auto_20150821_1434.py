# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20150821_1337'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='snippet',
            unique_together=set([('file_name', 'gist')]),
        ),
    ]
