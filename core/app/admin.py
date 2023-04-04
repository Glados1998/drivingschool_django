from django.contrib import admin
from .models import Course, User, Agency, Question, Quiz, HoursUser

# Register your models here.
admin.site.register(User)
admin.site.register(Agency)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(HoursUser)
