# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Penha',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='jugador',
            name='penha',
            field=models.ForeignKey(to='penhas.Penha'),
        ),
    ]
