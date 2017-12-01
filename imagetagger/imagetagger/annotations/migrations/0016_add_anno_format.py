# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0015_auto_20171129_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationFormat',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('field', JSONField(null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='annotationtype',
            name='format',
            field=models.ForeignKey(
                null=True,
                to='annotations.AnnotationFormat',
                on_delete=models.deletion.PROTECT,
                related_name='types'),
        ),
    ]
