# Generated by Django 3.1.1 on 2020-09-15 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('featured_image', models.ImageField(null=True, upload_to='')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('tags', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField()),
                ('featured', models.BooleanField()),
                ('block', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.category')),
            ],
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('description', models.CharField(max_length=255)),
                ('featured', models.BooleanField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=20)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('program', models.ManyToManyField(to='events.Program')),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.speaker'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.organiser'),
        ),
        migrations.AddField(
            model_name='event',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.person'),
        ),
        migrations.AddField(
            model_name='event',
            name='schedule',
            field=models.ManyToManyField(to='events.Schedule'),
        ),
    ]
