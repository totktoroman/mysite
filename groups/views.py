from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import *
from .models import Group
from .models import Student
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

    def get_success_url(self):
        return reverse_lazy('groups-detail', kwargs={'pk': self.object.group.id})
    template_name = 'groups/delete_student.html'

