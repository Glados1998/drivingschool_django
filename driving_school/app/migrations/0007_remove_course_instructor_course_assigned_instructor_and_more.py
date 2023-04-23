# Generated by Django 4.1.7 on 2023-04-22 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_user_assigned_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.AddField(
            model_name='course',
            name='assigned_instructor',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('role', 2)), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses_instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='assigned_student',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('role', 1)), null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses_student', to=settings.AUTH_USER_MODEL),
        ),
    ]