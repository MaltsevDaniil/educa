# Generated by Django 5.1.7 on 2025-06-12 10:00

import courses.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("courses", "0003_content_file_image_text_video"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content",
            options={"ordering": ["order"]},
        ),
        migrations.AlterModelOptions(
            name="module",
            options={"ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="content",
            name="order",
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="module",
            name="order",
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="content",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to={"model__in": ("text", "video", "image", "filead")},
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
    ]
