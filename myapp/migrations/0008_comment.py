# Generated by Django 3.2.8 on 2021-11-29 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20211129_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=1000)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.pet')),
            ],
        ),
    ]
