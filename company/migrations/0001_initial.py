# Generated by Django 5.0.6 on 2024-06-04 08:04

import filebrowser.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='company name')),
                ('logo', filebrowser.fields.FileBrowseField(max_length=255, verbose_name='company logo')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'company',
            },
        ),
    ]