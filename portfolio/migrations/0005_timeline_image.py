# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_timeline_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='image',
            field=models.ImageField(null=True, upload_to=b'timeline/', blank=True),
            preserve_default=True,
        ),
    ]
