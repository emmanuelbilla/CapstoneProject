from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import VolunteerAssignment
from .serializers import VolunteerAssignmentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsProjectOwnerOrReadOnly

# ViewSet for VolunteerAssignment
class VolunteerAssignmentViewSet(ModelViewSet):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer
    permission_classes = [IsProjectOwnerOrReadOnly] # Custom permission class