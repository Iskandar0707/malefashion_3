# Generated by Django 5.0.6 on 2024-06-24 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': '3. Brands',
                'db_table': 'Product brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': '2. Categories',
                'db_table': 'Product category',
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('code', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': '5. Colors',
                'db_table': 'Product color',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': '6. Tags',
                'db_table': 'Product tag',
            },
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': '4. Sizes',
                'db_table': 'Product size',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=60, verbose_name='title')),
                ('title_en', models.CharField(max_length=60, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=60, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=60, null=True, verbose_name='title')),
                ('title_de', models.CharField(max_length=60, null=True, verbose_name='title')),
                ('short_description', models.CharField(max_length=255, verbose_name='short description')),
                ('short_description_en', models.CharField(max_length=255, null=True, verbose_name='short description')),
                ('short_description_ru', models.CharField(max_length=255, null=True, verbose_name='short description')),
                ('short_description_uz', models.CharField(max_length=255, null=True, verbose_name='short description')),
                ('short_description_de', models.CharField(max_length=255, null=True, verbose_name='short description')),
                ('long_description', models.TextField(verbose_name='long description')),
                ('long_description_en', models.TextField(null=True, verbose_name='long description')),
                ('long_description_ru', models.TextField(null=True, verbose_name='long description')),
                ('long_description_uz', models.TextField(null=True, verbose_name='long description')),
                ('long_description_de', models.TextField(null=True, verbose_name='long description')),
                ('price', models.FloatField(verbose_name='price')),
                ('real_price', models.FloatField(default=0, verbose_name='real price')),
                ('sale', models.BooleanField(default=False, verbose_name='sale')),
                ('discount', models.PositiveSmallIntegerField(default=0, verbose_name='discount')),
                ('main_image', models.ImageField(upload_to='media/shop_product/%Y/%m/%d', verbose_name='main image')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='shop.brandmodel', verbose_name='brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='shop.category', verbose_name='category')),
                ('colors', models.ManyToManyField(related_name='products', to='shop.colormodel', verbose_name='colors')),
                ('tags', models.ManyToManyField(related_name='products', to='shop.producttag', verbose_name='tags')),
                ('sizes', models.ManyToManyField(related_name='products', to='shop.sizemodel', verbose_name='sizes')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': '1. Products',
                'db_table': 'Shop product',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productmodel', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Wishlist',
                'verbose_name_plural': 'Wishlists',
                'db_table': 'Wishlist',
            },
        ),
    ]