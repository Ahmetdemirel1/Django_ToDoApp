from django.contrib import admin
from .models import ToDo, UserRegister



class ToDoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'published_date']



admin.site.register(ToDo, ToDoAdmin)
