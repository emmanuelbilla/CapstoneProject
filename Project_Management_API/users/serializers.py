from rest_framework import serializers
from .models import User

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'