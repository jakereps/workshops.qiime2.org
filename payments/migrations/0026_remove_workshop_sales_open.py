# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0025_remove_workshop_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='sales_open',
        ),
    ]
