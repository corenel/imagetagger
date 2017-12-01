# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0016_add_anno_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationformat',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
