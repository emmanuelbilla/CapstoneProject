from rest_framework import serializers
from .models import VolunteerAssignment


# Serializer for VolunteerAssignment model
class VolunteerAssignmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = VolunteerAssignment
        fields = ['id', 'owner', 'user', 'task', 'joined_at']
        read_only_fields = ['owner', 'joined_at']