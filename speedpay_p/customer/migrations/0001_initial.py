# Generated by Django 4.0.3 on 2022-03-09 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='0f987305-a', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='customer-images/')),
                ('file', models.FileField(blank=True, null=True, upload_to='customer-files')),
                ('phone_number', models.CharField(max_length=17, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
