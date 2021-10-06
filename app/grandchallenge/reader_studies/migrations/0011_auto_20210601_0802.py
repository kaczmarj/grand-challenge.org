# Generated by Django 3.1.11 on 2021-06-01 08:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cases", "0003_auto_20210406_0753"),
        ("workstations", "0004_auto_20210512_1437"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("reader_studies", "0010_auto_20210512_1437"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="answer_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="cases.image",
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="reader_studies.question",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="reader_study",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="questions",
                to="reader_studies.readerstudy",
            ),
        ),
        migrations.AlterField(
            model_name="readerstudy",
            name="editors_group",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="editors_of_readerstudy",
                to="auth.group",
            ),
        ),
        migrations.AlterField(
            model_name="readerstudy",
            name="readers_group",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="readers_of_readerstudy",
                to="auth.group",
            ),
        ),
        migrations.AlterField(
            model_name="readerstudy",
            name="workstation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="workstations.workstation",
            ),
        ),
    ]
