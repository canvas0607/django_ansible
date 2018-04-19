# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('server', '0004_auto_20180410_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverdetail',
            name='server_group',
            field=models.ManyToManyField(blank=True, help_text='所属服务器组', to='project.SubProjectsServerGroup', verbose_name='所属服务器组'),
        ),
        migrations.AlterField(
            model_name='serverstatus',
            name='server',
            field=models.OneToOneField(help_text='对应服务器', on_delete=django.db.models.deletion.CASCADE, related_name='server_status', to='server.ServerDetail', verbose_name='对应服务器'),
        ),
    ]
