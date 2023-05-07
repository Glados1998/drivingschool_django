from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Course, TimeSlot, Exam, ExamQuestion, Answer


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': (
            'email', 'password', 'name', 'role', 'paid_course_hours', 'taken_course_hours', 'student_timeslots',
            'exam_status', 'assigned_instructor')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'role')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(TimeSlot)
admin.site.register(Exam)
admin.site.register(ExamQuestion)
admin.site.register(Answer)
