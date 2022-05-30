from django import forms
from .models import *
from django.shortcuts import get_object_or_404

class AddGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_number', 'group_title',]
        widgets = {
            'group_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер группы'
            }),
            'group_title': forms.Select(attrs={
                'class': 'form-select',
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group_title'].empty_value = "Категория не выбрана"

class AddStudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = ['student_surname', 'student_name','account_id', 'group']
        widgets = {
            'student_surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'group':forms.HiddenInput,
            'account_id': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'id Аккаунта'
             }),
        }

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = TaskAcmp
        fields = ['theme', 'level', 'task_list']
        widgets = {
            'theme': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тематика'
            }),
            'level': forms.Select(attrs={
                'class': 'form-select',
            }),
            'task_list': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номера задач    например:1, 2, 3, 4',
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['level'].empty_value = "Категория не выбрана"
