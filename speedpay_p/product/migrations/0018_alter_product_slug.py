# Generated by Django 4.0.3 on 2022-03-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='7d4d9511-5', editable=False, max_length=200),
        ),
    ]
