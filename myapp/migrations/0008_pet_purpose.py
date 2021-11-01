# Generated by Django 3.2.8 on 2021-11-01 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_pet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='purpose',
            field=models.CharField(choices=[('G', 'Give'), ('B', 'Breed')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]