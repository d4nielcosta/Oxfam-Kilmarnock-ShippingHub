# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_remove_text_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='volunteer',
        ),
    ]
