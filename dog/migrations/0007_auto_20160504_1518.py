# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0006_auto_20160504_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='doginfo',
            name='Author',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
