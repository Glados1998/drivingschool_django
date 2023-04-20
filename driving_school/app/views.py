from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserCreationForm, UserEditForm, CourseCreationForm, CourseEditForm, StudentCreationForm, \
    StudentEditForm, InstructorCreationForm, InstructorEditForm, \
    SecretaryCreationForm, SecretaryEditForm
from .models import Course, User


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'app/user-dashboard.html')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})


def user_panel(request):
    courses = Course.objects.all()
    all_users = User.objects.all()
    all_personal = User.objects.filter(role=2 | 3 | 4)
    students = User.objects.filter(role=1)
    instructors = User.objects.filter(role=2)
    admins = User.objects.filter(role=3)
    secretaries = User.objects.filter(role=4)
    return render(request, 'app/user-dashboard.html',
                  {'logged_in_user': request.user, 'course_add_form': CourseCreationForm, 'user_add_form': UserCreationForm,
                   'user_edit_form': UserEditForm, 'student_add_form': StudentCreationForm, 'instructor_add_form': InstructorCreationForm,
                   'instructor_edit_form': InstructorEditForm, 'secretary_add_form': SecretaryCreationForm,
                   'secretary_edit_form': SecretaryEditForm, 'courses': courses, 'students': students,
                   'instructors': instructors, 'admins': admins, 'secretaries': secretaries, 'all_users': all_users,
                   'all_personal': all_personal})


def logout_def(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, 'app/index.html')


def course_creation(request):
    if request.method == 'POST':
        course_add_form = CourseCreationForm(request.POST)
        if course_add_form.is_valid():
            course_add_form.save()
            return render(request, 'app/user-dashboard.html', {'course_add_form': course_add_form})
    else:
        course_add_form = CourseCreationForm()
    return render(request, 'app/user-dashboard.html', {'course_add_form': course_add_form})


def course_edit_delete(request, course_pk):
    instance = Course.objects.get(pk=course_pk)
    if 'edit' in request.POST:
        course_edit_form = CourseEditForm(request.POST, instance=instance)
        if course_edit_form.is_valid():
            course_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        course_edit_form = CourseEditForm(instance=instance)
    return render(request, 'crud/edit-courses.html', {'course_edit_form': course_edit_form})


def student_creation(request):
    if request.method == 'POST':
        student_add_form = StudentCreationForm(request.POST)
        if student_add_form.is_valid():
            student_add_form.save()
            return render(request, 'app/user-dashboard.html', {'student_add_form': student_add_form})
    else:
        student_add_form = StudentCreationForm()
    return render(request, 'app/user-dashboard.html', {'student_add_form': student_add_form})


def student_edit_delete(request, student_pk):
    instance = User.objects.get(pk=student_pk)
    if 'edit' in request.POST:
        student_edit_form = StudentEditForm(request.POST, instance=instance)
        if student_edit_form.is_valid():
            student_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        student_edit_form = StudentEditForm(instance=instance)
    return render(request, 'crud/edit-student.html', {'student_edit_form': student_edit_form})


def instructor_creation(request):
    if request.method == 'POST':
        instructor_add_form = InstructorCreationForm(request.POST)
        if instructor_add_form.is_valid():
            instructor_add_form.save()
            return render(request, 'app/user-dashboard.html', {'instructor_add_form': instructor_add_form})
    else:
        instructor_add_form = InstructorCreationForm()
    return render(request, 'app/user-dashboard.html', {'instructor_add_form': instructor_add_form})


def instructor_edit_delete(request, instructor_pk):
    instance = User.objects.get(pk=instructor_pk)
    if 'edit' in request.POST:
        instructor_edit_form = InstructorEditForm(request.POST, instance=instance)
        if instructor_edit_form.is_valid():
            instructor_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        instructor_edit_form = InstructorEditForm(instance=instance)
    return render(request, 'crud/edit-instructor.html', {'instructor_edit_form': instructor_edit_form})


def secretary_creation(request):
    if request.method == 'POST':
        secretary_add_form = SecretaryCreationForm(request.POST)
        if secretary_add_form.is_valid():
            secretary_add_form.save()
            return render(request, 'app/user-dashboard.html', {'secretary_add_form': secretary_add_form})
    else:
        secretary_add_form = SecretaryCreationForm()
    return render(request, 'app/user-dashboard.html', {'secretary_add_form': secretary_add_form})


def secretary_edit_delete(request, secretary_pk):
    instance = User.objects.get(pk=secretary_pk)
    if 'edit' in request.POST:
        secretary_edit_form = SecretaryEditForm(request.POST, instance=instance)
        if secretary_edit_form.is_valid():
            secretary_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        secretary_edit_form = SecretaryEditForm(instance=instance)
    return render(request, 'crud/edit-secretary.html', {'secretary_edit_form': secretary_edit_form})


def admin_creation(request):
    if request.method == 'POST':
        admin_add_form = UserCreationForm(request.POST)
        if admin_add_form.is_valid():
            admin_add_form.save()
            return render(request, 'app/user-dashboard.html', {'admin_add_form': admin_add_form})
    else:
        admin_add_form = UserCreationForm()
    return render(request, 'app/user-dashboard.html', {'admin_add_form': admin_add_form})


def admin_edit_delete(request, admin_pk):
    instance = User.objects.get(pk=admin_pk)
    if 'edit' in request.POST:
        admin_edit_form = UserEditForm(request.POST, instance=instance)
        if admin_edit_form.is_valid():
            admin_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        admin_edit_form = UserEditForm(instance=instance)
    return render(request, 'crud/edit-admin.html', {'admin_edit_form': admin_edit_form})
