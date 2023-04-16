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
            'is_active': forms.Select(attrs={'class': 'form-control'}),
            'assigned_courses': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'password', 'email', 'name', 'role', 'assigned_courses'}
        exclude = {'is_active'}
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'assigned_courses': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
