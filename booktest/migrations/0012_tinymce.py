# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0011_auto_20180115_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='TinyMce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'tinymce',
            },
        ),
    ]
