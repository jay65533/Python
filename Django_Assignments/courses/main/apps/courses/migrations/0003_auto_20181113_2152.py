# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-14 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181113_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='courses',
            new_name='course',
        ),
    ]
