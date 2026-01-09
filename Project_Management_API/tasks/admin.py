from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'owner', 'status', 'is_completed')
    list_filter = ('status', 'is_completed')
    search_fields = ('title', )