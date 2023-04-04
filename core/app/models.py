from django.db import models


# Create your models here.

class Course(models.Model):
    course_hours = models.IntegerField(null=True)
    course_date = models.DateField()
    course_duration = models.DurationField()
    course_place = models.CharField(max_length=50)
    course_instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_instructor.first_name + " " + self.course_instructor.last_name + " " + self.course_date + " " + self.course_duration


class Student(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    courses = models.ManyToManyField(Course)
    hours_of_taken_courses = models.IntegerField(null=True)
    hours_of_paid_courses = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Instructor(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Secretary(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Admin(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name
