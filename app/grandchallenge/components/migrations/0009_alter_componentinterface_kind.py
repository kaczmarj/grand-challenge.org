# Generated by Django 3.2.10 on 2022-02-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("components", "0008_alter_componentinterfacevalue_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="componentinterface",
            name="kind",
            field=models.CharField(
                choices=[
                    ("STR", "String"),
                    ("INT", "Integer"),
                    ("FLT", "Float"),
                    ("BOOL", "Bool"),
                    ("JSON", "Anything"),
                    ("CHART", "Chart"),
                    ("2DBB", "2D bounding box"),
                    ("M2DB", "Multiple 2D bounding boxes"),
                    ("DIST", "Distance measurement"),
                    ("MDIS", "Multiple distance measurements"),
                    ("POIN", "Point"),
                    ("MPOI", "Multiple points"),
                    ("POLY", "Polygon"),
                    ("MPOL", "Multiple polygons"),
                    ("LINE", "Line"),
                    ("MLIN", "Multiple lines"),
                    ("CHOI", "Choice"),
                    ("MCHO", "Multiple choice"),
                    ("IMG", "Image"),
                    ("SEG", "Segmentation"),
                    ("HMAP", "Heat Map"),
                    ("PDF", "PDF file"),
                    ("SQREG", "SQREG file"),
                    ("JPEG", "Thumbnail jpg"),
                    ("PNG", "Thumbnail png"),
                    ("CSV", "CSV file"),
                    ("ZIP", "ZIP file"),
                ],
                help_text="What is the type of this interface? Used to validate interface values and connections between components.",
                max_length=5,
            ),
        ),
    ]
