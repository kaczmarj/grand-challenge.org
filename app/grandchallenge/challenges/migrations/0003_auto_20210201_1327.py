# Generated by Django 3.1.1 on 2021-02-01 13:27

from django.db import migrations, models

import grandchallenge.core.storage


class Migration(migrations.Migration):

    dependencies = [("challenges", "0002_auto_20201217_0653")]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="social_image",
            field=models.ImageField(
                blank=True,
                help_text="An image for this challenge which is displayed when you post the link on social media. Should have a resolution of 640x320 px (1280x640 px for best display).",
                storage=grandchallenge.core.storage.PublicS3Storage(),
                upload_to=grandchallenge.core.storage.get_social_image_path,
            ),
        ),
        migrations.AddField(
            model_name="externalchallenge",
            name="social_image",
            field=models.ImageField(
                blank=True,
                help_text="An image for this challenge which is displayed when you post the link on social media. Should have a resolution of 640x320 px (1280x640 px for best display).",
                storage=grandchallenge.core.storage.PublicS3Storage(),
                upload_to=grandchallenge.core.storage.get_social_image_path,
            ),
        ),
    ]
