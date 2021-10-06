# Generated by Django 3.1.11 on 2021-07-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0008_evaluation_input_prefixes"),
    ]

    operations = [
        migrations.RemoveField(model_name="submission", name="creators_ip",),
        migrations.RemoveField(
            model_name="submission", name="creators_user_agent",
        ),
        migrations.AddField(
            model_name="submission",
            name="staged_predictions_file_uuid",
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
    ]
