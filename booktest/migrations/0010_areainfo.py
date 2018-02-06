# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0009_bookinfo_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('areaTitle', models.CharField(max_length=20)),
                ('areaPid', models.ForeignKey(to='booktest.AreaInfo', db_column=b'pid')),
            ],
            options={
                'db_table': 'areainfo',
            },
        ),
    ]
