# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='level',
            field=models.IntegerField(default=1, help_text=b'Nivel Prioridad Sponsor', choices=[(1, b'Gold'), (2, b'Platinum')]),
            preserve_default=False,
        ),
    ]
