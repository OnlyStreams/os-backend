# Generated by Django 4.2 on 2023-05-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stream", "0004_streamprofile_is_streaming_streamprofile_viewers"),
    ]

    operations = [
        migrations.AddField(
            model_name="streamprofile",
            name="url",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
