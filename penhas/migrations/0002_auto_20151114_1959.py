# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penhas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jugador',
            options={'ordering': ['penha']},
        ),
        migrations.AlterModelOptions(
            name='penha',
            options={'ordering': ['nombre']},
        ),
    ]
