# Generated by Django 2.2.4 on 2019-08-26 09:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0013_rawimageuploadsession_reader_study"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("algorithms", "0008_auto_20190508_1325"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Algorithm", new_name="AlgorithmImage"
        ),
        migrations.RenameField(
            model_name="job", old_name="algorithm", new_name="algorithm_image"
        ),
    ]
