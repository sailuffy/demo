# Generated by Django 4.1.4 on 2022-12-26 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_review_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]