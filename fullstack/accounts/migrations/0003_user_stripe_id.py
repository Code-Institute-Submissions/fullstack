# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-20 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]