# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0012_tinymce'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.ImageField(upload_to=b'booktest/')),
            ],
            options={
                'db_table': 'pictureinfo',
            },
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d'),
        ),
    ]
