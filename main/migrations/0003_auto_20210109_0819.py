# Generated by Django 3.1.1 on 2021-01-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]
