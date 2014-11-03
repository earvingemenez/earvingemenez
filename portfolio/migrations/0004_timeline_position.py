# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_timeline_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='position',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
