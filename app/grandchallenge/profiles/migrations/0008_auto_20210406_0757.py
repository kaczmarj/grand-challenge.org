# Generated by Django 3.1.6 on 2021-04-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0007_auto_20210331_1646")]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="notifications_last_read_at",
            field=models.DateTimeField(auto_now_add=True),
        )
    ]
