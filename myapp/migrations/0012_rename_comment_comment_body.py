# Generated by Django 3.2.8 on 2021-11-29 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20211129_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
    ]