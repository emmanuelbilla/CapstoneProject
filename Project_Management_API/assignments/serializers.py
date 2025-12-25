from rest_framework import serializers
from .models import VolunteerAssignment


# Serializer for VolunteerAssignment model
class VolunteerAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerAssignment
        fields = '__all__'