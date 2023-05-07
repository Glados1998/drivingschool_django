from django import forms
from .models import Course, User, TimeSlot, Exam, ExamQuestion, Answer, StudentAnswer


class CourseForm(forms.ModelForm):
    time_slot = forms.ModelChoiceField(queryset=TimeSlot.objects.filter(is_available=True))

    class Meta:
        model = Course
        fields = ['location', 'assigned_instructor', 'assigned_student', 'time_slot']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned_instructor': forms.Select(attrs={'class': 'form-control'}),
            'assigned_student': forms.Select(attrs={'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
        }

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
                  'taken_course_hours', 'assigned_instructor'}
        exclude = {'role'}
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'student_timeslots': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'paid_course_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'taken_course_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'assigned_instructor': forms.Select(attrs={'class': 'form-control'}),
        },
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'is_active': 'Active',
            'student_timeslots': 'Time Slots',
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'role': 'Role',
            'is_active': 'Active',
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long'
        }


class SecretaryForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'is_active'}
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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
        labels = {
            'title': 'Title',
        }


class ExamQuestionForm(forms.ModelForm):
    class Meta:
        model = ExamQuestion
        fields = ['exam_question', 'exam']
        widgets = {
            'exam_question': forms.TextInput(attrs={'class': 'form-control'}),
            'exam': forms.Select(attrs={'class': 'form-control'}),
        },
        labels = {
            'exam_question': 'Question',
            'exam': 'Exam',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct', 'exam_question']
        widgets = {
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'exam_question': forms.Select(attrs={'class': 'form-control'}),
        },
        labels = {
            'answer': 'Answer',
            'is_correct': 'Correct',
            'exam_question': 'Question',
        }
