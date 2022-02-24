# Generated by Django 3.1.6 on 2021-03-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0005_auto_20210213_1330")]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="display_organizations",
            field=models.BooleanField(
                default=True,
                help_text="Display the organizations that you are a member of in your profile.",
            ),
        )
    ]
