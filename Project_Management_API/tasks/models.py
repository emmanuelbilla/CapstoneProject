from django.db import models
from projects.models import Project

# Create your models here.
class Task(models.Model):
    # ForeignKey to Project model
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    # Task fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # String representation of the Task
        return f"{self.title} - {'Completed' if self.is_completed else 'Pending'}"