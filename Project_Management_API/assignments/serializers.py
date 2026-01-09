from rest_framework import serializers
from .models import VolunteerAssignment


# Serializer for VolunteerAssignment model
class VolunteerAssignmentSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # Automatically set the owner to the logged-in user

    class Meta:
        model = VolunteerAssignment
        fields = '__all__'  # Include all fields of the model
    
def validate(self, data):
    if VolunteerAssignment.objects.filter(
        user=data['user'],
        task=data['task']
    ).exists():
        raise serializers.ValidationError("This user is already assigned to this task.")
    return data