# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-13 02:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0003_auto_20181112_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninjas',
            old_name='dojo',
            new_name='dojos',
        ),
    ]