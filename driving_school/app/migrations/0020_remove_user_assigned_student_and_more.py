# Generated by Django 4.1.7 on 2023-05-07 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_user_assigned_instructor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='assigned_student',
        ),
        migrations.AddField(
            model_name='user',
            name='assigned_instructor',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('role', 2)), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_instructor', to=settings.AUTH_USER_MODEL),
        ),
    ]
