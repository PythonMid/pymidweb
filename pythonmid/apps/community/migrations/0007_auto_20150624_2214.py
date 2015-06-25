# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20150624_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_organizer',
            new_name='is_member',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, max_length=1000, help_text='Breve biografía', null=True),
        ),
    ]
