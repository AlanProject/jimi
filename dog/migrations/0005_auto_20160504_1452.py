# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 06:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0004_doginfo_author'),
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
