# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0006_auto_20180103_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='aParent',
            new_name='aPid',
        ),
    ]
