from django.contrib import admin
from .models import Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'start_date', 'end_date')
    list_filter = ('status', )
    search_fields = ('title', )
    