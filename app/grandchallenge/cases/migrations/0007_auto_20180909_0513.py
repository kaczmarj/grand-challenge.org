# Generated by Django 2.0.8 on 2018-09-09 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("algorithms", "0002_auto_20180909_0513"),
        ("cases", "0006_auto_20180830_1524"),
    ]

    operations = [
        migrations.AddField(
            model_name="rawimageuploadsession",
            name="algorithm",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="algorithms.Algorithm",
            ),
        ),
        migrations.AddField(
            model_name="rawimageuploadsession",
            name="algorithm_result",
            field=models.OneToOneField(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="algorithms.Result",
            ),
        ),
        migrations.AddField(
            model_name="rawimageuploadsession",
            name="creator",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
