# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-13 02:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0004_auto_20181112_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninjas',
            name='dojos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas.Dojos'),
        ),
    ]
