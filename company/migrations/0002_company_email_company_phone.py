# Generated by Django 5.0.6 on 2024-06-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='company email address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default='', max_length=20, verbose_name='company phone number'),
            preserve_default=False,
        ),
    ]