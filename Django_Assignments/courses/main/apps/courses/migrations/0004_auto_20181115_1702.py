# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-16 01:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20181113_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='course',
            new_name='moss',
        ),
    ]
