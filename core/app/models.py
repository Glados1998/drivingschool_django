from django.db import models


# Create your models here.

class Course(models.Model):
    course_appointment = models.DateTimeField(null=True)
    course_duration = models.DurationField()
    course_place = models.CharField(max_length=50)
    course_attending_user = models.ForeignKey('User', on_delete=models.CASCADE, limit_choices_to={'role': 1}, related_name='student+', null=True)
    course_attending_instructor = models.ForeignKey('User', on_delete=models.CASCADE, limit_choices_to={'role': 2}, related_name='instructor+', null=True)
    agency_object = models.ForeignKey('Agency', on_delete=models.PROTECT, null=True)

class User(models.Model):
    STUDENT = 1
    INSTRUCTOR = 2
    ADMIN = 3
    SECRETARY = 4

    USER_ROLES = (
        (STUDENT, 'Student'),
        (INSTRUCTOR, 'Instructor'),
        (ADMIN, 'Admin'),
        (SECRETARY, 'Secretary'),
    )

    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    role = models.PositiveSmallIntegerField(choices=USER_ROLES, default=1, null=True)
    agency = models.ForeignKey('Agency', on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Agency(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    zipcode = models.CharField(max_length=10)


class Quiz(models.Model):
    instructor = models.ForeignKey('User', on_delete=models.PROTECT)
    questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.course.course_instructor.first_name + " " + self.course.course_instructor.last_name + " " + self.course.course_date + " " + self.course.course_duration


class Question(models.Model):
    related_quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class HoursUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    remaining_hours = models.IntegerField(null=True)
    used_hours = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.remaining_hours + " " + self.used_hours
