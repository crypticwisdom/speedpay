# Generated by Django 4.0.3 on 2022-03-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_alter_customer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default='1de7b4e4-6', max_length=100),
        ),
    ]