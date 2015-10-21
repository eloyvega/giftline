# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intercambio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('publico', models.BooleanField(default=False)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('intercambio', models.ForeignKey(to='intercambios.Intercambio')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='intercambio',
            name='participantes',
            field=models.ManyToManyField(through='intercambios.Lista', to=settings.AUTH_USER_MODEL),
        ),
    ]
