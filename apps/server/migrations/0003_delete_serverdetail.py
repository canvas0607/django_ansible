# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 03:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_serverdetail_ssh_port'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServerDetail',
        ),
    ]
