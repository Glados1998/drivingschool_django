from django import forms
from .models import Course, User, TimeSlot, Exam, ExamQuestion, Answer, StudentAnswer


class CourseForm(forms.ModelForm):
    time_slot = forms.ModelChoiceField(queryset=TimeSlot.objects.filter(is_available=True))

    class Meta:
        model = Course
        fields = ['location', 'assigned_instructor', 'assigned_student', 'time_slot']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.assigned_student:
            self.fields['time_slot'].queryset = self.instance.assigned_student.student_timeslots.filter(
                is_available=True)
        elif 'assigned_student' in self.data:
            try:
                student = User.objects.get(id=self.data['assigned_student'])
                self.fields['time_slot'].queryset = student.student_timeslots.filter(is_available=True)
            except (ValueError, User.DoesNotExist):
                pass


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'is_active', 'student_timeslots', 'paid_course_hours',
                  'taken_course_hours'}
        exclude = {'role'}
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        },
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'is_active': 'Active',
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long',
            'email': 'Please enter a valid email address',
            'name': 'Please enter a valid name',
            'is_active': 'Please select if the user is active',
        },
        error_messages = {
            'password': {
                'min_length': 'Password must be at least 8 characters long',
            },
            'email': {

                'invalid': 'Please enter a valid email address',
            },
            'name': {
                'invalid': 'Please enter a valid name',
            },
            'role': {
                'invalid': 'Please select a valid role',
            },
            'is_active': {

                'invalid': 'Please select if the user is active',
            },
        }


class InstructorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'is_active'}
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'role': 'Role',
            'is_active': 'Active',
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long',
            'email': 'Please enter a valid email address',
            'name': 'Please enter a valid name',
            'is_active': 'Please select if the user is active',
        }


class SecretaryForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'is_active'}
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'is_active': 'Active',
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long',
            'email': 'Please enter a valid email address',
            'name': 'Please enter a valid name',
            'is_active': 'Please select if the user is active',
            'assigned_courses': 'Please select at least one course',
        }


class AdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'is_active'}
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'is_active': forms.CheckboxInput(),
        }
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'is_active': 'Active',
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long',
            'email': 'Please enter a valid email address',
            'name': 'Please enter a valid name',
            'is_active': 'Please select if the user is active',
            'assigned_courses': 'Please select at least one course',
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        },


class ExamQuestionForm(forms.ModelForm):
    class Meta:
        model = ExamQuestion
        fields = ['exam_question', 'exam']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct', 'exam_question']
