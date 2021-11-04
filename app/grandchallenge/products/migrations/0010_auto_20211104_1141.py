# Generated by Django 3.1.13 on 2021-11-04 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("products", "0009_auto_20210831_0957"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="editors_group",
            field=models.OneToOneField(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="editors_of_company",
                to="auth.group",
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="initial_editor",
            field=models.EmailField(default="default", max_length=254),
            preserve_default=False,
        ),
    ]
