# Generated by Django 4.0.3 on 2022-03-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_customer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default='f084576f-a', max_length=100),
        ),
    ]