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