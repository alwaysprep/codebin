# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20150820_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, upload_to='profiles', null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='theme',
            field=models.CharField(default='monokai', max_length=64, choices=[('ambiance', 'ambiance'), ('chaos', 'chaos'), ('chrome', 'chrome'), ('clouds', 'clouds'), ('clouds_midnight', 'clouds_midnight'), ('cobalt', 'cobalt'), ('crimson_editor', 'crimson_editor'), ('dawn', 'dawn'), ('dreamweaver', 'dreamweaver'), ('eclipse', 'eclipse'), ('github', 'github'), ('idle_fingers', 'idle_fingers'), ('iplastic', 'iplastic'), ('katzenmilch', 'katzenmilch'), ('kr_theme', 'kr_theme'), ('kuroir', 'kuroir'), ('merbivore', 'merbivore'), ('merbivore_soft', 'merbivore_soft'), ('mono_industrial', 'mono_industrial'), ('monokai', 'monokai'), ('pastel_on_dark', 'pastel_on_dark'), ('solarized_dark', 'solarized_dark'), ('solarized_light', 'solarized_light'), ('sqlserver', 'sqlserver'), ('terminal', 'terminal'), ('textmate', 'textmate'), ('tomorrow', 'tomorrow'), ('tomorrow_night', 'tomorrow_night'), ('tomorrow_night_blue', 'tomorrow_night_blue'), ('tomorrow_night_bright', 'tomorrow_night_bright'), ('tomorrow_night_eighties', 'tomorrow_night_eighties'), ('twilight', 'twilight'), ('vibrant_ink', 'vibrant_ink'), ('xcode', 'xcode')]),
        ),
    ]
