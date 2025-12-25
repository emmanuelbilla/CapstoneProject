from django.db import models
from users.models import User
from projects.models import Project

# Create your models here.
class VolunteerAssignment(models.Model):
    # ForeignKey to User model
    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        related_name='assignments'
    )

    # ForeignKey to Project model
    project = models.ForeignKey(
        Project,
        on_delete= models.CASCADE,
        related_name='assignments'
    )
    joined_at = models.DateTimeField(auto_now_add=True) # Timestamp when the volunteer joined the project

    # String representation of the VolunteerAssignment
    class Meta:
        unique_together = ('user', 'project')


    def __str__(self):
        return f"{self.user.name} assigned to {self.project.title}"