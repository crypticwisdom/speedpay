# Generated by Django 4.0.3 on 2022-03-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_brand_alter_product_slug_delete_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='e60ba3bd-c', max_length=200),
        ),
    ]