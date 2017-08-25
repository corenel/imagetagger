# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 09:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170825_1114'),
        ('images', '0003_auto_20170825_1012'),
    ]

    def forward_func(apps, schema_editor):
        ImageSet = apps.get_model("images", "ImageSet")
        Team = apps.get_model("users", "Team")

        db_alias = schema_editor.connection.alias

        # make sure there are no duplicate team names
        for team in Team.objects.using(db_alias).all():
            used_names = set()
            for image_set in ImageSet.objects.using(db_alias).filter(team=team):
                while image_set.name in used_names:
                    image_set.name += 'FIXED'
                    if image_set.name not in used_names:
                        break
                image_set.save()
                used_names.add(image_set.name)

    def backward_func(apps, schema_editor):
        raise NotImplementedError

    operations = [
        migrations.RunPython(forward_func, backward_func, atomic=True),
        migrations.AlterModelOptions(
            name='imageset',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='imageset',
            unique_together=set([('name', 'team')]),
        ),
    ]
