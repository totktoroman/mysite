from django.shortcuts import render, redirect

from .forms import *
from .models import Group
from .models import Student
from django import forms
from django.http import HttpResponse
from django.views.generic import DeleteView

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
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups_home')
    else:
        form = AddGroupForm()
    return render(request, 'groups/add_group.html', {'form': form, 'title': 'Создание группы'})

def delete_group(DeleteView):
    model = Group
    success_url='groups_home'
    template_name = 'groups/delete_group.html'
def edit_group(request, group_id):
    return HttpResponse(f"<h1> Редактирование группы № {group_id}  </h1>")