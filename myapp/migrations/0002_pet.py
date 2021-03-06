# Generated by Django 3.2.8 on 2021-11-01 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], max_length=1)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=10)),
            ],
        ),
    ]
