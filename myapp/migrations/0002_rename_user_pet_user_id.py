# Generated by Django 3.2.8 on 2021-11-21 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='user',
            new_name='user_id',
        ),
    ]