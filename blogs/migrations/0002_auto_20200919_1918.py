# Generated by Django 3.0.6 on 2020-09-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='event_static/images/blog_images'),
        ),
    ]