from django.urls import path
from . import views
urlpatterns = [
    path('', views.groups_home, name='groups_home'),
    path('<int:group_id>', views.selected_group, name='groups-detail'),

    path('add_group', views.add_group, name='add_group'),
    path('delete_group/<int:group_id>/', views.delete_group, name='delete_group'),

    path('edit_group/<int:group_id>/', views.edit_group, name='edit_group'),

]