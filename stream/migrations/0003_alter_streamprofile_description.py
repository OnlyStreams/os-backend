# Generated by Django 4.2 on 2023-05-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stream", "0002_streamprofile_stream_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="streamprofile",
            name="description",
            field=models.TextField(blank=True, default="", max_length=512),
        ),
    ]
