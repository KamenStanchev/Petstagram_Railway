# Generated by Django 4.1.4 on 2022-12-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='pet_photos/', verbose_name='Pet image'),
        ),
    ]
