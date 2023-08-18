# Generated by Django 4.2.4 on 2023-08-17 21:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150, verbose_name="Nombre")),
                (
                    "rut",
                    models.CharField(max_length=9, unique=True, verbose_name="RUT"),
                ),
                (
                    "fecha_registro",
                    models.DateField(
                        default=datetime.datetime.now, verbose_name="Fecha de registro"
                    ),
                ),
                ("fecha_creacion", models.DateTimeField(auto_now=True)),
                ("fecha_actualización", models.DateTimeField(auto_now_add=True)),
                ("correo", models.CharField(max_length=150, verbose_name="Correo")),
            ],
            options={
                "verbose_name": "Administrador",
                "verbose_name_plural": "Administradores",
                "db_table": "dministrador",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="comunidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150, verbose_name="Nombre")),
                ("vertientes", models.PositiveIntegerField(default=0)),
                (
                    "ubicación",
                    models.CharField(max_length=200, verbose_name="Ubicación"),
                ),
            ],
            options={
                "verbose_name": "Comunidad",
                "verbose_name_plural": "Comunidades",
                "db_table": "comunidad",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="vertiente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150, verbose_name="Nombre")),
                ("desc", models.CharField(max_length=250, verbose_name="Descripcion")),
                (
                    "ubicación",
                    models.CharField(max_length=200, verbose_name="Ubicación"),
                ),
                ("caudal", models.IntegerField(default=0)),
                ("pH", models.IntegerField(default=0)),
                ("conductividad", models.IntegerField(default=0)),
                ("turbiedad", models.IntegerField(default=0)),
                ("temperatura", models.IntegerField(default=0)),
                ("humedad", models.IntegerField(default=0)),
                (
                    "comunidad",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="iniciosesion.comunidad",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vertiente",
                "verbose_name_plural": "Vertientes",
                "db_table": "vertiente",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150, verbose_name="Nombre")),
                (
                    "rut",
                    models.CharField(max_length=9, unique=True, verbose_name="RUT"),
                ),
                (
                    "fecha_registro",
                    models.DateField(
                        default=datetime.datetime.now, verbose_name="Fecha de registro"
                    ),
                ),
                ("fecha_creacion", models.DateTimeField(auto_now=True)),
                ("fecha_actualización", models.DateTimeField(auto_now_add=True)),
                ("edad", models.PositiveIntegerField(default=0)),
                ("correo", models.CharField(max_length=150, verbose_name="Correo")),
                (
                    "comunidad",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="iniciosesion.comunidad",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuario",
                "verbose_name_plural": "Usuarios",
                "db_table": "usuario",
                "ordering": ["id"],
            },
        ),
    ]