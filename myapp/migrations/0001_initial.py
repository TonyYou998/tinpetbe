# Generated by Django 3.2.8 on 2021-11-21 23:31

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
            name='demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('quanntity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=6)),
                ('age', models.PositiveIntegerField()),
                ('race', models.CharField(choices=[('D', 'Dog'), ('C', 'Cat'), ('O', 'Other')], max_length=6)),
                ('type', models.CharField(max_length=20)),
                ('purpose', models.CharField(choices=[('G', 'Give'), ('B', 'Breed')], max_length=6)),
                ('location', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='img/%y')),
                ('owner', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
