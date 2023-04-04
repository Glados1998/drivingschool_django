# Generated by Django 4.2 on 2023-04-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_courses_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_hours',
        ),
        migrations.AddField(
            model_name='course',
            name='course_date_hour_of_appointment',
            field=models.DateTimeField(null=True),
        ),
    ]
