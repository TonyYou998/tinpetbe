# Generated by Django 3.2.8 on 2021-11-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_pet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='img/%y'),
        ),
    ]
