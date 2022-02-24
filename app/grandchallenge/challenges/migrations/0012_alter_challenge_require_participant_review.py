# Generated by Django 3.2.10 on 2022-02-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0011_challenge_access_request_handling")]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="require_participant_review",
            field=models.BooleanField(
                default=False,
                help_text="If ticked, new participants need to be approved by project admins before they can access restricted pages. If not ticked, new users are allowed access immediately",
                null=True,
            ),
        )
    ]
