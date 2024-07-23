# Generated by Django 4.2.14 on 2024-07-23 10:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_home_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_card',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='home_card',
            name='img_homeCard',
            field=models.ImageField(upload_to='images/'),
        ),
    ]