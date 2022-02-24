# Generated by Django 3.1.1 on 2020-12-02 13:08

import uuid

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("cases", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="OctObsRegistration",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "registration_values",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=django.contrib.postgres.fields.ArrayField(
                            base_field=models.FloatField(), size=2
                        ),
                        size=2,
                    ),
                ),
                (
                    "obs_image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="obs_image",
                        to="cases.image",
                    ),
                ),
                (
                    "oct_image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oct_image",
                        to="cases.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("obs_image", "oct_image")},
            },
        )
    ]
