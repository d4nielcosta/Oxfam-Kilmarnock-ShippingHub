# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_auto_20150612_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='name',
        ),
    ]
