# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20180419_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputeHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='机房名称', max_length=100, verbose_name='机房名称')),
                ('address', models.CharField(help_text='机房地址', max_length=300, verbose_name='机房地址')),
            ],
            options={
                'verbose_name': '机房信息',
                'verbose_name_plural': '机房信息',
            },
        ),
        migrations.AddField(
            model_name='serverdetail',
            name='compute_house',
            field=models.ForeignKey(blank=True, default=None, help_text='机房信息', on_delete=django.db.models.deletion.CASCADE, to='server.ComputeHouse', verbose_name='机房信息'),
            preserve_default=False,
        ),
    ]
