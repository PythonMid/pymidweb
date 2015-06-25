# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='from_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 6, 5, 55, 110822, tzinfo=utc), help_text=b'Fecha y hora de inicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='to_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 6, 5, 55, 110822, tzinfo=utc), help_text=b'Fecha y hora de finalizaci\xc3\xb3n'),
            preserve_default=False,
        ),
    ]
