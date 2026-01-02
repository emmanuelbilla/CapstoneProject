from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task

# Create your models here.
class VolunteerAssignment(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='volunteer_assignments'
        ) # The user who created the assignment
    
    # ForeignKey to User model
    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name='assignments'
    )

    # ForeignKey to Task model
    task = models.ForeignKey(
        Task,
        on_delete= models.CASCADE,
        related_name='assignments'
    )

    joined_at = models.DateTimeField(auto_now_add=True) # Timestamp when the volunteer joined the project

    # String representation of the VolunteerAssignment
    class Meta:
        unique_together = ('user', 'task')  # Ensure a user can be assigned to a task only once


    def __str__(self):
        return f"{self.user.username} assigned to {self.task.title}"