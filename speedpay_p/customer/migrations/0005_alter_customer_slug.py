# Generated by Django 4.0.3 on 2022-03-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default='e4960775-d', max_length=100),
        ),
    ]
