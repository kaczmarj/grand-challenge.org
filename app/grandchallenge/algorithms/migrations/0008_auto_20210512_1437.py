# Generated by Django 3.1.9 on 2021-05-12 14:37

import stdimage.models
from django.db import migrations

import grandchallenge.core.storage


class Migration(migrations.Migration):
    dependencies = [("algorithms", "0007_auto_20210402_1508")]

    operations = [
        migrations.AlterField(
            model_name="algorithm",
            name="logo",
            field=stdimage.models.JPEGField(
                storage=grandchallenge.core.storage.PublicS3Storage(),
                upload_to=grandchallenge.core.storage.get_logo_path,
            ),
        ),
        migrations.AlterField(
            model_name="algorithm",
            name="social_image",
            field=stdimage.models.JPEGField(
                blank=True,
                help_text="An image for this algorithm which is displayed when you post the link for this algorithm on social media. Should have a resolution of 640x320 px (1280x640 px for best display).",
                storage=grandchallenge.core.storage.PublicS3Storage(),
                upload_to=grandchallenge.core.storage.get_social_image_path,
            ),
        ),
    ]
