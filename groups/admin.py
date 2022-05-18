from django.contrib import admin
from .models import Group
from .models import Student

# Register your models here.
admin.site.register(Group)
admin.site.register(Student)