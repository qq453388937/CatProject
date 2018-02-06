# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0008_auto_20180104_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='pic',
            field=models.ImageField(default=None, upload_to=b'upload/'),
        ),
    ]
