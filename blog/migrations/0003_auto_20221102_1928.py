# Generated by Django 3.2.16 on 2022-11-02 19:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221102_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipspost',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Feautured Image'),
        ),
        migrations.AlterField(
            model_name='tipspost',
            name='stance_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Stance Image'),
        ),
        migrations.AlterField(
            model_name='tipspost',
            name='swing_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Swing Image'),
        ),
    ]
