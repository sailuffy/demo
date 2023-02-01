# Generated by Django 4.1.4 on 2022-12-20 23:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_alter_profile_id_alter_skill_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('website_link', models.CharField(blank=True, max_length=100, null=True)),
                ('manga_link', models.CharField(blank=True, max_length=100, null=True)),
                ('project_image', models.ImageField(blank=True, default='monkey.jpg', null=True, upload_to='')),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.CharField(choices=[('Up', 'up_vote'), ('down', 'down_vote')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='project.tag'),
        ),
    ]
