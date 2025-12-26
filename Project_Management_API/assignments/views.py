from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import VolunteerAssignment
from .serializers import VolunteerAssignmentSerializer

# List and Create Assignments
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer

# Retrieve, Update, and Delete an Assignment
class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer