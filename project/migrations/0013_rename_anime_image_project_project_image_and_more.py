# Generated by Django 4.1.4 on 2023-01-29 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_rename_project_image_project_anime_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='anime_image',
            new_name='project_image',
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 23, 33, 49, 503502)),
        ),
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 23, 33, 49, 503502)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 23, 33, 49, 503502)),
        ),
    ]
