# Generated by Django 4.1.4 on 2022-12-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
