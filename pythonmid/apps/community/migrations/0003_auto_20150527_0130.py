# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_sponsor_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='image',
            new_name='logo',
        ),
    ]
