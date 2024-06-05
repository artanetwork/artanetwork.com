# Generated by Django 5.0.6 on 2024-06-04 14:51

import filebrowser.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='product name')),
                ('category', models.CharField(choices=[('AC', 'Active'), ('PA', 'Passive'), ('WI', 'Wireless'), ('CA', 'CCTV Camera'), ('TO', 'Tower'), ('PO', 'Power')], max_length=2, verbose_name='product category')),
                ('description', models.TextField(verbose_name='product description')),
                ('image', filebrowser.fields.FileBrowseField(max_length=2255, verbose_name='product image')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]