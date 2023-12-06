# Generated by Django 5.0 on 2023-12-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Nombre"
                    ),
                ),
                (
                    "instructions",
                    models.TextField(
                        blank=True, null=True, verbose_name="Instrucciones"
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(blank=True, null=True, verbose_name="Duración"),
                ),
                ("ingredients", models.ManyToManyField(to="foods.food")),
            ],
        ),
    ]
