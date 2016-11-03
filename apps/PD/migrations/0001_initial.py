# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingredientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingrediente', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='resetas',
            fields=[
                ('nombre', models.CharField(max_length=64, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='ingredientes',
            name='reseta',
            field=models.ForeignKey(to='PD.resetas'),
        ),
    ]
