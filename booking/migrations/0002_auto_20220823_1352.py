# Generated by Django 3.2.15 on 2022-08-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='car_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]