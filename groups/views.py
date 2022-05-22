from django.shortcuts import render, redirect

from .forms import *
from .models import Group
from .models import Student
from django import forms
from django.http import HttpResponse
from django.views.generic import DeleteView, UpdateView

from django.views.generic import DetailView
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

    fields = ['group_number', 'group_title']

class delete_group(DeleteView):
    model = Group
    success_url = '/groups/'
    template_name = 'groups/delete_group.html'

