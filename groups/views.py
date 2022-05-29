from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import DeleteView, UpdateView, DetailView

import requests
from bs4 import BeautifulSoup

# Create your views here.
def groups_home(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups_home.html', {'groups': groups})

def selected_group(request, pk):
    students = Student.objects.filter(group_id=pk)
    groups = Group.objects.filter(id=pk)
    context = {
        'students': students,
        'groups': groups,
    }
    return render(request, 'groups/groups_students.html', context=context)

def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups_home')
    else:
        form = AddGroupForm()
    return render(request, 'groups/add_group.html', {'form': form, 'title': 'Создание группы'})

class edit_group(UpdateView):
    model = Group
    template_name = 'groups/edit_group.html'
    form_class = AddGroupForm

class delete_group(DeleteView):
    model = Group
    success_url = '/groups/'
    template_name = 'groups/delete_group.html'


def add_student(request, pk):
    if request.method == 'POST':
        form = AddStudentForm(request.POST, pk)
        if form.is_valid():
            form.save()
            return redirect('groups-detail', pk)
    else:
        form = AddStudentForm()
    data = {
        'form': form,
        'group_id': pk,
    }
    return render(request, 'groups/add_student.html', data)

class edit_student(UpdateView):
    model = Student
    template_name = 'groups/edit_student.html'
    form_class = AddStudentForm

class delete_student(DeleteView):
    model = Student
    template_name = 'groups/delete_student.html'
    def get_success_url(self):
        return reverse_lazy('groups-detail', kwargs={'pk': self.object.group.id})

def task_home(request):
    task = TaskAcmp.objects.all()
    return render(request, 'groups/task_home.html', {'task': task})

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_home')
    else:
        form = AddTaskForm()
    return render(request, 'groups/add_task.html', {'form': form, 'title': 'Добавление новых задач'})

class edit_task(UpdateView):
    model = TaskAcmp
    template_name = 'groups/edit_task.html'
    form_class = AddTaskForm

class delete_task(DeleteView):
    model = TaskAcmp
    success_url = '/groups/task_home'
    template_name = 'groups/delete_task.html'



def student_statistic(request, pk):
    student = Student.objects.get(id=pk)
    url = f'https://acmp.ru/index.asp?main=user&id={student.account_id}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    cp = soup.findAll("p")
    complete_tasks = cp[1].findAll('a')
    failed_tasks = cp[2].findAll('a')

    complete_tasks_numbers=[]
    for item in complete_tasks:
        complete_tasks_numbers.append(item.text)

    failed_tasks_numbers = []
    for item in failed_tasks:
        failed_tasks_numbers.append(item.text)

    context = {
        'student': student,
        'complete_tasks': complete_tasks_numbers,
        'failed_tasks': failed_tasks_numbers,
    }
    return render(request, 'groups/student_statistic.html', context=context)
