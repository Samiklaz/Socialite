# Generated by Django 3.0.7 on 2020-06-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0007_remove_like_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
