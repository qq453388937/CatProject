# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='aParent',
            field=models.ForeignKey(db_column=b'pid', blank=True, to='booktest.Area', null=True),
        ),
    ]
