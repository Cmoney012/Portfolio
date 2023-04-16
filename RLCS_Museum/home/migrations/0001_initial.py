# Generated by Django 4.1.6 on 2023-03-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('team_one', models.CharField(default='', max_length=100)),
                ('team_one_score', models.IntegerField(default='0')),
                ('team_two', models.CharField(default='', max_length=100)),
                ('team_two_score', models.IntegerField(default='0')),
                ('event', models.CharField(max_length=100)),
                ('date_of_event', models.DateField()),
                ('pregame', models.TextField(default='')),
                ('game1', models.TextField(default='')),
                ('game2', models.TextField(default='')),
                ('game3', models.TextField(default='')),
                ('game4', models.TextField(default='')),
                ('game5', models.TextField(default='')),
                ('game6', models.TextField(default='')),
                ('postgame', models.TextField(default='')),
            ],
        ),
    ]
