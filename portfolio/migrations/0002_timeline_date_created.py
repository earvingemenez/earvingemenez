# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2014, 11, 2, 0, 35, 27, 747466, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
