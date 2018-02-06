# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0010_areainfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='areaPid',
            field=models.ForeignKey(db_column=b'pid', blank=True, to='booktest.AreaInfo', null=True),
        ),
    ]
