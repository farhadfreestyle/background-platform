# Generated by Django 5.0 on 2023-12-29 22:14

import experience.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to=experience.models.experience_image_upload_path)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
