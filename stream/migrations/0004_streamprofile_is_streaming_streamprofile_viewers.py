# Generated by Django 4.2 on 2023-05-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stream", "0003_alter_streamprofile_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="streamprofile",
            name="is_streaming",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="streamprofile",
            name="viewers",
            field=models.IntegerField(default=0),
        ),
    ]
