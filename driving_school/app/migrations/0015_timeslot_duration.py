# Generated by Django 4.1.7 on 2023-04-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_course_time_slot_remove_user_student_timeslots_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
