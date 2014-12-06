# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('echo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='successWebhook',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
