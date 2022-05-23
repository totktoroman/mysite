from django.template.defaulttags import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.groups_home, name='groups_home'),
    path('<int:pk>/', views.selected_group, name='groups-detail'),
    path('add_group', views.add_group, name='add_group'),
    path('<int:pk>/edit_group', views.edit_group.as_view(), name='edit_group'),
    path('<int:pk>/delete_group', views.delete_group.as_view(), name='delete_group'),

    path('<int:pk>/add_student', views.add_student, name='add_student'),
    path('student-<int:pk>/edit_student', views.edit_student.as_view(), name='edit_student'),
    path('student-<int:pk>/delete_student', views.delete_student.as_view(), name='delete_student'),
]