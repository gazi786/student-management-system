# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveIntegerField(choices=[(1, 'Advisor'), (2, 'Staff'), (3, 'Executive Staff')], default=1, verbose_name='Role'),
            preserve_default=False,
        ),
    ]
