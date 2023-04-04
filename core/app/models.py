from django.db import models


# Create your models here.

class Course(models.Model):
    appointment = models.DateTimeField(null=True)
    duration = models.DurationField()
    place = models.CharField(max_length=50)
    student = models.ForeignKey('User', on_delete=models.PROTECT)
    instructor = models.ForeignKey('User', on_delete=models.PROTECT)
    agency = models.ForeignKey('Agency', on_delete=models.PROTECT)

    def __str__(self):
        return self.instructor.first_name + " " + self.instructor.last_name + " " + self.appointment + " " + self.duration


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
    courses = models.ManyToManyField(Course)
    role = models.PositiveSmallIntegerField(choices=USER_ROLES, default=1, null=True)
    agency = models.ForeignKey('Agency', on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Agency(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    courses = models.ManyToManyField(Course)
    zipcode = models.CharField(max_length=10)


class Quiz(models.Model):
    instructor = models.ForeignKey('User', on_delete=models.PROTECT)
    questions = models.ManyToManyField('Question')

    def __str__(self):
        return self.course.course_instructor.first_name + " " + self.course.course_instructor.last_name + " " + self.course.course_date + " " + self.course.course_duration


class Question(models.Model):
    question = models.CharField(max_length=200)
    answers = models.ManyToManyField('Answer')

    def __str__(self):
        return self.question


class HoursUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    remaining_hours = models.IntegerField(null=True)
    used_hours = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.remaining_hours + " " + self.used_hours
