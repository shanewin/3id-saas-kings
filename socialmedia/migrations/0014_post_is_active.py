# Generated by Django 4.2.1 on 2023-09-21 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("socialmedia", "0013_alter_post_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
