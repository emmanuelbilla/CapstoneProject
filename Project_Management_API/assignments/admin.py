from django.contrib import admin
from .models import VolunteerAssignment

# Register your models here.
@admin.register(VolunteerAssignment)
class VolunteerAssignmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'owner', 'joined_at')
    search_fields = ('user__username', 'task__title', )