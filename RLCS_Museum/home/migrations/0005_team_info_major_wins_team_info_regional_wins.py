# Generated by Django 4.1.6 on 2023-03-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_team_info_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_info',
            name='major_wins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team_info',
            name='regional_wins',
            field=models.IntegerField(default=0),
        ),
    ]
