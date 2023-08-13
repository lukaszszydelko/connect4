# Generated by Django 3.2.13 on 2023-07-20 14:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Connect4Game",
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
                (
                    "current_player",
                    models.CharField(
                        choices=[("o", "o"), ("x", "x"), ("_", "_")],
                        default="o",
                        max_length=1,
                    ),
                ),
                (
                    "board",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=django.contrib.postgres.fields.ArrayField(
                            base_field=models.CharField(
                                choices=[("o", "o"), ("x", "x"), ("_", "_")],
                                default="_",
                                max_length=1,
                            ),
                            size=7,
                        ),
                        size=7,
                    ),
                ),
                (
                    "winner",
                    models.CharField(
                        choices=[("o", "o"), ("x", "x"), ("_", "_")],
                        default="_",
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]