# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 06:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_auto_20180228_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverdetail',
            name='last_scan_time',
        ),
    ]
