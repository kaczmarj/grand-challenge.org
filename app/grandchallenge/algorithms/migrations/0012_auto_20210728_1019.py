# Generated by Django 3.1.13 on 2021-07-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("algorithms", "0011_job_input_prefixes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "Queued"),
                    (1, "Started"),
                    (2, "Re-Queued"),
                    (3, "Failed"),
                    (4, "Succeeded"),
                    (5, "Cancelled"),
                    (6, "Provisioning"),
                    (7, "Provisioned"),
                    (8, "Executing"),
                    (9, "Executed"),
                    (10, "Parsing Outputs"),
                    (11, "Executing Algorithm"),
                ],
                db_index=True,
                default=0,
            ),
        ),
    ]
