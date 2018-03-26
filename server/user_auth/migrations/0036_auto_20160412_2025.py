# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 20:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0035_auto_20160411_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knackuser',
            name='reasons',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=["I'm an awesome knacker", 'Who absolutely loves what I do', "I'm fun, fair and honest", "I'll do a great job everytime", "you'll really love your knack"]),
        ),
    ]
