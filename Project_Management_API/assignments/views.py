from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import VolunteerAssignment
from .serializers import VolunteerAssignmentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.permissions import IsOwnerOrReadOnly
from .permissions import IsProjectOwnerOrReadOnly

# List and Create Assignments
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer
    permission_classes = [IsProjectOwnerOrReadOnly] # Allow read-only access for unauthenticated users

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, Update, and Delete an Assignment
class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer
    permission_classes = [IsProjectOwnerOrReadOnly] # Allows only owners to edit or delete

# ViewSet for VolunteerAssignment
class VolunteerAssignmentViewSet(ModelViewSet):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer
    permission_classes = [IsProjectOwnerOrReadOnly] # Custom permission class