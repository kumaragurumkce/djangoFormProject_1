# Generated by Django 4.2.14 on 2024-07-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_card_title', models.CharField(max_length=20)),
                ('img_homeCard', models.FileField(upload_to='pic/%y/')),
            ],
        ),
    ]
