# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=50)),
                ('megusta', models.IntegerField(default=0, editable=False)),
                ('slug', models.SlugField(default=b'', unique=True)),
            ],
            options={
                'ordering': ['penha'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Penha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('visitas', models.IntegerField(default=0, editable=False)),
                ('direccion', models.CharField(max_length=70)),
                ('slug', models.SlugField(default=b'', unique=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='jugador',
            name='penha',
            field=models.ForeignKey(to='partidos_penha.Penha'),
            preserve_default=True,
        ),
    ]
