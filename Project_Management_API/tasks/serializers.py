from rest_framework import serializers
from .models import Task

# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # Automatically set the owner to the logged-in user
    
    class Meta:
        model = Task
        fields = '__all__'