# Generated by Django 3.1.13 on 2021-10-12 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploads", "0004_auto_20211012_0957"),
        ("evaluation", "0014_method_user_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="user_upload",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="uploads.userupload",
            ),
        ),
    ]
