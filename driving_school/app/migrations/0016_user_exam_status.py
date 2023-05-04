# Generated by Django 4.1.7 on 2023-05-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_timeslot_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='exam_status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'passed'), (2, 'failed'), (3, 'not concerned')], null=True),
        ),
    ]