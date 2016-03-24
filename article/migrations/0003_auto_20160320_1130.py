# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151220_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='commentary_author',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='commentary',
            name='commentary_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='commentary_text',
            field=models.TextField(verbose_name='Commentary text:'),
        ),
    ]
