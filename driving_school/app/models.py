from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.db.models import Q


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    STUDENT = 1
    INSTRUCTOR = 2
    ADMIN = 3
    SECRETARY = 4
    USER_ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (INSTRUCTOR, 'Instructor'),
        (ADMIN, 'Admin'),
        (SECRETARY, 'Secretary'),
    ]

    PASSED = 1
    FAILED = 2
    NOT_CONCERNED = 3

    ExamStatus = [
        (PASSED, 'passed'),
        (FAILED, 'failed'),
        (NOT_CONCERNED, 'not concerned'),
    ]

    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, blank=True, null=True)
    exam_status = models.PositiveSmallIntegerField(choices=ExamStatus, blank=True, null=True)
    paid_course_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taken_course_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    student_timeslots = models.ManyToManyField('TimeSlot', blank=True, related_name='students')
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    assigned_instructor = models.ForeignKey('User', on_delete=models.SET_NULL, related_name='student_instructor', null=True, blank=True, limit_choices_to=Q(role=2))

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk


class Course(models.Model):
    location = models.CharField(max_length=254)
    assigned_instructor = models.ForeignKey('User', on_delete=models.SET_NULL, related_name='courses_instructor',
                                            null=True, blank=True, limit_choices_to=Q(role=2))
    assigned_student = models.ForeignKey('User', on_delete=models.SET_NULL, related_name='courses_student', null=True,
                                         blank=True, limit_choices_to=Q(role=1))
    time_slot = models.ForeignKey('TimeSlot', on_delete=models.SET_NULL, related_name='courses_timeslot', null=True,
                                  blank=True)

    def __str__(self):
        return f'{self.location}'

    def get_student_details(self):
        return self.assigned_student

    def get_instructor_details(self):
        return self.assigned_instructor

    def cancel_course_for_student(self, user):
        # Check if the user is a student and is assigned to this course
        if user.role == 1 and self.assigned_student == user:
            # Set the assigned_student field to None
            self.assigned_student = None

            # Make the time slot available again
            if self.time_slot:
                self.time_slot.is_available = True
                self.time_slot.save()

            self.time_slot = None
            self.save()  # Save the changes to the course
            return True  # Indicate that the course was successfully canceled
        return False  # Indicate that the course could not be canceled

    def free_timeslot(self):
        if self.time_slot:
            self.time_slot.is_available = True
            self.time_slot.save()
            return True
        return False


class TimeSlot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.start_time} - {self.end_time}' + f' ({self.duration} hours)'

    def calculate_duration(self):
        duration_seconds = (self.end_time - self.start_time).total_seconds()
        duration_hours = duration_seconds / 3600
        return round(duration_hours, 2)

    def save(self, *args, **kwargs):
        self.duration = self.calculate_duration()
        super().save(*args, **kwargs)


class Exam(models.Model):
    title = models.CharField(max_length=254)


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    exam_question = models.CharField(max_length=254)


class Answer(models.Model):
    exam_question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=254)
    is_correct = models.BooleanField(default=False)


class StudentAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
