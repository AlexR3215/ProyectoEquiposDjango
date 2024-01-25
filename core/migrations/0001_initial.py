# Generated by Django 5.0.1 on 2024-01-25 08:22

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de la competición')),
                ('lugar', models.CharField(max_length=30, verbose_name='Lugar de la competición')),
                ('fechaCreacion', models.DateField(default=datetime.date.today, verbose_name='fecha de creacion')),
                ('fechaModificacion', models.DateField(default=datetime.date.today, verbose_name='fecha de modificacion')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imgCompeticion')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Competicion',
            },
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del equipo')),
                ('categoria', models.CharField(max_length=30, verbose_name='Nombre de la categoría')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imgEquipo')),
                ('fechaCreacion', models.DateField(default=datetime.date.today, verbose_name='fecha de creacion')),
                ('fechaModificacion', models.DateField(default=datetime.date.today, verbose_name='fecha de modificacion')),
                ('competicion', models.ManyToManyField(to='core.competicion', verbose_name='Competicion')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Equipos',
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del Jugador')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('edad', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imgJugador')),
                ('fechaCreacion', models.DateField(default=datetime.date.today, verbose_name='fecha de creacion')),
                ('fechaModificacion', models.DateField(default=datetime.date.today, verbose_name='fecha de modificacion')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipos')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Jugadores',
            },
        ),
    ]
