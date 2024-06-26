# Generated by Django 5.0.6 on 2024-06-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('collection', models.CharField(max_length=60, verbose_name='collection')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('description', models.TextField(max_length=100, verbose_name='description')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='image')),
                ('is_active', models.BooleanField(blank=True, default=False, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='MainSM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('description', models.TextField(max_length=255, verbose_name='description')),
                ('tag', models.CharField(max_length=60, verbose_name='tag')),
                ('url', models.URLField(verbose_name='link')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Medias',
            },
        ),
        migrations.CreateModel(
            name='MainSMImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='MainSM/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Social Media Image',
                'verbose_name_plural': 'Social Media Images',
            },
        ),
    ]
