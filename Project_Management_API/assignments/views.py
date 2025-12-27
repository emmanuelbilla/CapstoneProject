from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import VolunteerAssignment
from .serializers import VolunteerAssignmentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# List and Create Assignments
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read-only access for unauthenticated users

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, Update, and Delete an Assignment
class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer