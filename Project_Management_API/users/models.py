from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('coordinator', 'Coordinator'),
        ('volunteer', 'Volunteer'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='volunteer'
                            )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.role})"