# Generated by Django 3.2.10 on 2022-02-17 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reader_studies", "0015_auto_20220210_1106"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="readerstudy", name="image_port_mapping",
        ),
    ]
