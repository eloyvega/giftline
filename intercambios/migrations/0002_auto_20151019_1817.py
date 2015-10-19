# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('intercambios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='miembros',
            name='intercambio',
        ),
        migrations.RemoveField(
            model_name='miembros',
            name='user',
        ),
        migrations.AlterField(
            model_name='intercambio',
            name='participantes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='intercambios.Lista'),
        ),
        migrations.DeleteModel(
            name='Miembros',
        ),
        migrations.AddField(
            model_name='lista',
            name='intercambio',
            field=models.ForeignKey(to='intercambios.Intercambio'),
        ),
        migrations.AddField(
            model_name='lista',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
