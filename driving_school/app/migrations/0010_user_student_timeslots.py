# Generated by Django 4.1.7 on 2023-04-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_timeslots',
            field=models.ManyToManyField(blank=True, to='app.timeslot'),
        ),
    ]
