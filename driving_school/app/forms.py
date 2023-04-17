from django import forms
from .models import Course, User


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'role', 'is_active', 'assigned_courses'}
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
            'assigned_courses': forms.SelectMultiple(attrs={'class': 'form-control'}),
        },
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'role': 'Role',
            'is_active': 'Active',
            'assigned_courses': 'Assigned Courses',
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long',
            'email': 'Please enter a valid email address',
            'name': 'Please enter a valid name',
            'role': 'Please select a valid role',
            'is_active': 'Please select if the user is active',
            'assigned_courses': 'Please select at least one course',
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
            'assigned_courses': {
                'invalid': 'Please select at least one course',
            },
        }


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'role', 'assigned_courses'}
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
            'assigned_courses': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'password': 'Password',
            'email': 'Email',
            'name': 'Name',
            'role': 'Role',
            'is_active': 'Active',
            'assigned_courses': 'Assigned Courses',
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long',
            'email': 'Please enter a valid email address',
            'name': 'Please enter a valid name',
            'role': 'Please select a valid role',
            'is_active': 'Please select if the user is active',
            'assigned_courses': 'Please select at least one course',
        }
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
            'assigned_courses': {
                'invalid': 'Please select at least one course',
            },
        }
