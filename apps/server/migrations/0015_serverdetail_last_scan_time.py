# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_remove_serverdetail_last_scan_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverdetail',
            name='last_scan_time',
            field=models.DateTimeField(help_text='上次扫描时间', null=True, verbose_name='上次扫描时间'),
        ),
    ]
