from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserForm, CourseForm, StudentForm, InstructorForm, \
    SecretaryForm, AdminForm, ExamForm, ExamQuestionForm, AnswerForm
from .models import Course, User, Exam, ExamQuestion, Answer


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
    instructor_user = request.user
    instructor_courses = Course.objects.filter(assigned_instructor=instructor_user)
    student_user = request.user
    student_courses = Course.objects.filter(assigned_student=student_user)
    courses = Course.objects.all()
    all_users = User.objects.all()
    exams = Exam.objects.all()
    assigned_students = User.objects.filter(assigned_instructor=request.user)
    exam_questions = ExamQuestion.objects.all()
    answers = Answer.objects.all()
    all_personal = User.objects.filter(role=2 | 3 | 4)
    students = User.objects.filter(role=1)
    instructors = User.objects.filter(role=2)
    admins = User.objects.filter(role=3)
    secretaries = User.objects.filter(role=4)
    return render(request, 'app/user-dashboard.html',
                  {'logged_in_user': request.user, 'course_add_form': CourseForm,
                   'user_add_form': UserCreationForm,
                   'user_edit_form': UserForm, 'student_add_form': StudentForm,
                   'instructor_add_form': InstructorForm, 'exam_add_form': ExamForm,
                   'exam_question_add_form': ExamQuestionForm,
                   'answer_add_form': AnswerForm, 'instructor_edit_form': InstructorForm,
                   'secretary_add_form': InstructorForm,
                   'secretary_edit_form': InstructorForm, 'courses': courses, 'students': students,
                   'instructors': instructors, 'admins': admins, 'secretaries': secretaries, 'all_users': all_users,
                   'all_personal': all_personal, 'instructor_courses': instructor_courses,
                   'student_courses': student_courses, 'exams': exams, 'exam_questions': exam_questions,
                   'answers': answers, 'assigned_students': assigned_students})


def logout_def(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, 'app/index.html')


def course_creation(request):
    if request.method == 'POST':
        course_add_form = CourseForm(request.POST)
        if course_add_form.is_valid():
            course = course_add_form.save(commit=False)

            time_slot = course_add_form.cleaned_data['time_slot']
            time_slot.is_available = False
            time_slot.save()
            course.save()
            return render(request, 'app/user-dashboard.html')
    else:
        course_add_form = CourseForm()
    return render(request, 'settings/instructor/instructor-cours-add.html', {'course_add_form': course_add_form})


def course_edit_delete(request, course_pk):
    instance = Course.objects.get(pk=course_pk)
    if 'edit' in request.POST:
        course_edit_form = CourseForm(request.POST, instance=instance)
        if course_edit_form.is_valid():
            course = course_edit_form.save(commit=False)

            old_time_slot = instance.time_slot
            new_time_slot = course_edit_form.cleaned_data['time_slot']
            if old_time_slot != new_time_slot:
                old_time_slot.is_available = True
                old_time_slot.save()
                new_time_slot.is_available = False
                new_time_slot.save()

            course.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        time_slot = instance.time_slot
        time_slot.is_available = True
        time_slot.save()
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        course_edit_form = CourseForm(instance=instance)
    return render(request, 'crud/edit-courses.html', {'course_edit_form': course_edit_form})


def student_creation(request):
    if request.method == 'POST':
        student_add_form = StudentForm(request.POST)
        if student_add_form.is_valid():
            new_student = student_add_form.save(commit=False)
            new_student.role = 1
            new_student.save()
            return render(request, 'app/user-dashboard.html')
    else:
        student_add_form = StudentForm()
    return render(request, 'settings/secretary/secretary-student-add.html', {'student_add_form': student_add_form})


def student_edit_delete(request, student_pk):
    instance = User.objects.get(pk=student_pk)
    if 'edit' in request.POST:
        student_edit_form = StudentForm(request.POST, instance=instance)
        if student_edit_form.is_valid():
            student_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        student_edit_form = StudentForm(instance=instance)
    return render(request, 'crud/edit-student.html', {'student_edit_form': student_edit_form})


def instructor_creation(request):
    if request.method == 'POST':
        instructor_add_form = InstructorForm(request.POST)
        if instructor_add_form.is_valid():
            new_instructor = instructor_add_form.save(commit=False)
            new_instructor.role = 2
            new_instructor.save()
            return render(request, 'app/user-dashboard.html')
    else:
        instructor_add_form = InstructorForm()
    return render(request, 'settings/secretary/secretary-instructor-add.html',
                  {'instructor_add_form': instructor_add_form})


def instructor_edit_delete(request, instructor_pk):
    instance = User.objects.get(pk=instructor_pk)
    if 'edit' in request.POST:
        instructor_edit_form = InstructorForm(request.POST, instance=instance)
        if instructor_edit_form.is_valid():
            instructor_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        instructor_edit_form = InstructorForm(instance=instance)
    return render(request, 'crud/edit-instructor.html', {'instructor_edit_form': instructor_edit_form})


def secretary_creation(request):
    if request.method == 'POST':
        secretary_add_form = SecretaryForm(request.POST)
        if secretary_add_form.is_valid():
            new_secretary = secretary_add_form.save(commit=False)
            new_secretary.role = 4
            new_secretary.is_staff = True
            new_secretary.save()
            return render(request, 'app/user-dashboard.html')
    else:
        secretary_add_form = SecretaryForm()
    return render(request, 'settings/admin/admin-secretary-add.html', {'secretary_add_form': secretary_add_form})


def secretary_edit_delete(request, secretary_pk):
    instance = User.objects.get(pk=secretary_pk)
    if 'edit' in request.POST:
        secretary_edit_form = SecretaryForm(request.POST, instance=instance)
        if secretary_edit_form.is_valid():
            secretary_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        secretary_edit_form = SecretaryForm(instance=instance)
    return render(request, 'crud/edit-secretary.html', {'secretary_edit_form': secretary_edit_form})


def admin_creation(request):
    if request.method == 'POST':
        admin_add_form = UserForm(request.POST)
        if admin_add_form.is_valid():
            admin_add_form.save()
            return render(request, 'app/user-dashboard.html')
    else:
        admin_add_form = UserCreationForm()
    return render(request, 'settings/admin/admin-user-add.html', {'admin_add_form': admin_add_form})


def admin_edit_delete(request, admin_pk):
    instance = User.objects.get(pk=admin_pk)
    if 'edit' in request.POST:
        admin_edit_form = UserForm(request.POST, instance=instance)
        if admin_edit_form.is_valid():
            admin_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        admin_edit_form = UserForm(instance=instance)
    return render(request, 'crud/edit-admin.html', {'admin_edit_form': admin_edit_form})


def student_details(request, student_pk):
    instance = User.objects.get(pk=student_pk)
    student_courses = Course.objects.filter(assigned_student=instance)
    return render(request, 'settings/shared/student-details.html',
                  {'student': instance, 'student_courses': student_courses})


def instructor_details(request, instructor_pk):
    instructor = User.objects.get(pk=instructor_pk)
    instructor_courses = Course.objects.filter(assigned_instructor=instructor).exclude(assigned_student=None)
    return render(request, 'settings/shared/instructor-details.html',
                  {'instructor': instructor, 'instructor_courses': instructor_courses})


def cancelCourse(request, course_pk):
    student = User.objects.get(pk=request.user.pk)
    course = Course.objects.get(pk=course_pk)
    result = course.cancel_course_for_student(student)
    if result:
        messages.success(request, 'Course canceled successfully.')
    else:
        messages.error(request, 'Failed to cancel the course.')
    return render(request, 'app/user-dashboard.html')


def complete_course(request, course_pk):
    course = Course.objects.get(pk=course_pk)
    student = User.objects.get(pk=request.user.pk)
    if student.role != User.STUDENT:
        messages.error(request, 'Only students can complete courses.')
        return render(request, 'app/user-dashboard.html')

    if course.assigned_student != student:
        messages.error(request, 'Student is not assigned to the course.')
        return render(request, 'app/user-dashboard.html')
    course_duration = course.time_slot.duration

    if student.paid_course_hours < course_duration:
        messages.error(request, 'Student does not have enough paid course hours.')
        return render(request, 'app/user-dashboard.html')

    student.paid_course_hours -= course_duration
    student.taken_course_hours += course_duration

    course.delete()
    student.save()
    messages.success(request, 'Course completed successfully.')
    return render(request, 'app/user-dashboard.html')


def createExam(request):
    if request.method == 'POST':
        exam_add_form = ExamForm(request.POST)
        if exam_add_form.is_valid():
            new_exam = exam_add_form.save(commit=False)
            new_exam.save()
            return render(request, 'app/user-dashboard.html')
    else:
        exam_add_form = ExamForm()
    return render(request, 'app/user-dashboard.html', {'exam_add_form': exam_add_form})


def editDeleteExam(request, exam_pk):
    instance = Exam.objects.get(pk=exam_pk)
    if 'edit' in request.POST:
        exam_edit_form = ExamForm(request.POST, instance=instance)
        if exam_edit_form.is_valid():
            exam_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        exam_edit_form = ExamForm(instance=instance)
    return render(request, 'crud/edit-exam.html', {'exam_edit_form': exam_edit_form})


def createExamQuestion(request):
    if request.method == 'POST':
        exam_question_add_form = ExamQuestionForm(request.POST)
        if exam_question_add_form.is_valid():
            new_exam_question = exam_question_add_form.save(commit=False)
            new_exam_question.save()
            return render(request, 'app/user-dashboard.html')
    else:
        exam_question_add_form = ExamQuestionForm()
    return render(request, 'app/user-dashboard.html', {'exam_question_add_form': exam_question_add_form})


def editDeleteQuestion(request, question_pk):
    instance = ExamQuestion.objects.get(pk=question_pk)
    if 'edit' in request.POST:
        exam_question_edit_form = ExamQuestionForm(request.POST, instance=instance)
        if exam_question_edit_form.is_valid():
            exam_question_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        exam_question_edit_form = ExamQuestionForm(instance=instance)
    return render(request, 'crud/edit-question.html', {'exam_question_edit_form': exam_question_edit_form})


def createExamAnswer(request):
    if request.method == 'POST':
        exam_answer_add_form = AnswerForm(request.POST)
        if exam_answer_add_form.is_valid():
            new_exam_answer = exam_answer_add_form.save(commit=False)
            new_exam_answer.save()
            return render(request, 'app/user-dashboard.html')
    return render(request, 'app/user-dashboard.html')


def editDeleteAnswer(request, answer_pk):
    instance = Answer.objects.get(pk=answer_pk)
    if 'edit' in request.POST:
        exam_answer_edit_form = AnswerForm(request.POST, instance=instance)
        if exam_answer_edit_form.is_valid():
            exam_answer_edit_form.save()
            return render(request, 'app/user-dashboard.html')
    elif 'delete' in request.POST:
        instance.delete()
        return render(request, 'app/user-dashboard.html')
    else:
        exam_answer_edit_form = AnswerForm(instance=instance)
    return render(request, 'crud/edit-answer.html', {'exam_answer_edit_form': exam_answer_edit_form})


def exam_menu(request):
    exams = Exam.objects.all()
    return render(request, 'app/exam-menu.html', {'exams': exams})


def start_exam(request, exam_pk):
    exam = Exam.objects.get(pk=exam_pk)
    exam_questions = exam.examquestion_set.all()
    context = {'exam': exam, 'exam_questions': exam_questions}
    return render(request, 'app/exam.html', context)


def submit_exam(request, exam_pk):
    user = request.user
    if request.method != 'POST':
        return redirect('app:exam_menu')

    exam = get_object_or_404(Exam, pk=exam_pk)
    exam_questions = exam.examquestion_set.all()

    correct_answers = 0
    incorrect_answers = 0

    for question in exam_questions:
        user_answer_id = request.POST.get(f'question_{question.pk}')
        if not user_answer_id:
            continue

        user_answer = Answer.objects.get(pk=user_answer_id)
        if user_answer.is_correct:
            correct_answers += 1
        else:
            incorrect_answers += 1
    if correct_answers >= incorrect_answers:
        messages.success(request, 'Congratulations! You passed the exam.')
        user.exam_status = User.PASSED
        user.save()
        return render(request, 'app/user-dashboard.html')
    else:
        messages.error(request, 'Sorry! You failed the exam.')
        user.exam_status = User.FAILED
        user.save()
        return render(request, 'app/user-dashboard.html')
