# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170517_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='inventory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='periodic_tasks', related_query_name='periodic_tasks', to='main.Inventory'),
            preserve_default=False,
        ),
    ]
