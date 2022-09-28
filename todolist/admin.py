from django.contrib import admin

# Register your models here.

from .models import Task, Task_Form

admin.site.register(Task)