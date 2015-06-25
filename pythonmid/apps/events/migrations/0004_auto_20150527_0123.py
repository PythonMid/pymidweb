# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendee',
            options={'verbose_name': 'Asistentes', 'verbose_name_plural': 'Asistentes'},
        ),
    ]
