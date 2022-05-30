from django.template.defaulttags import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.groups_home, name='groups_home'),
    path('<int:pk>/', views.selected_group, name='groups-detail'),
    path('add_group', views.add_group, name='add_group'),
    path('<int:pk>/edit_group', views.edit_group.as_view(), name='edit_group'),
    path('<int:pk>/delete_group', views.delete_group.as_view(), name='delete_group'),
    path('<int:pk>/', views.update_parse, name='update_parse'),

    path('student-<int:pk>/statistic', views.student_statistic, name='student_statistic'),
    path('<int:pk>/add_student', views.add_student, name='add_student'),
    path('student-<int:pk>/edit_student', views.edit_student.as_view(), name='edit_student'),
    path('student-<int:pk>/delete_student', views.delete_student.as_view(), name='delete_student'),


    path('task_home', views.task_home, name='task_home'),
    path('add_task', views.add_task, name='add_task'),
    path('<int:pk>/edit_task', views.edit_task.as_view(), name='edit_task'),
    path('<int:pk>/delete_task', views.delete_task.as_view(), name='delete_task'),
]