from django.shortcuts import render
from .models import Group
from .models import Student
from django import forms
from django.http import HttpResponse

from django.views.generic import DetailView
# Create your views here.
def groups_home(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups_home.html', {'groups': groups})

def selected_group(request, group_id):
    students = Student.objects.filter(group_id=group_id)
    groups = Group.objects.filter(id=group_id)

    context = {
        'students': students,
        'groups': groups,
    }
    return render(request, 'groups/groups_students.html', context=context)

def add_group(request):



    return render(request, 'groups/add_group.html')
def delete_group(request, group_id):
    return HttpResponse(f"<h1> Удаление группы № {group_id}, возможно только при отсутсвии студентов в таковой! </h1>")
def edit_group(request, group_id):
    return HttpResponse(f"<h1> Редактирование группы № {group_id}  </h1>")