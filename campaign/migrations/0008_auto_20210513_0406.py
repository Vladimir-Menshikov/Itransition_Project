# Generated by Django 3.0.5 on 2021-05-13 01:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0007_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created',), 'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
