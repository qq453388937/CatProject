# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20180103_0004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heroinfo',
            options={'ordering': ['id']},
        ),
    ]
