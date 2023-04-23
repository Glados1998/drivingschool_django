# Generated by Django 4.1.7 on 2023-04-23 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_course_selected_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time_slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses_timeslot', to='app.timeslot'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='student_timeslots',
        ),
        migrations.AddField(
            model_name='user',
            name='student_timeslots',
            field=models.ManyToManyField(blank=True, related_name='students', to='app.timeslot'),
        ),
    ]