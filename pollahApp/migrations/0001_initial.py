# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pollah_answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer_text', models.CharField(max_length=1023)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='pollah_question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question_text', models.CharField(max_length=1023)),
                ('time_created', models.DateTimeField(verbose_name='Time Created')),
            ],
        ),
        migrations.AddField(
            model_name='pollah_answer',
            name='question',
            field=models.ForeignKey(to='pollahApp.pollah_question'),
        ),
    ]
