# Generated by Django 3.0.7 on 2020-06-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0004_auto_20200613_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='connection',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
