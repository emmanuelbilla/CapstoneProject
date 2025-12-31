import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date

from projects.models import Project
from tasks.models import Task
from assignments.models import VolunteerAssignment

@pytest.mark.django_db
class TestAssignmentsAPI:
    def setup_method(self):

        self.client = APIClient()

        # Create users
        self.owner = User.objects.create_user(
            username='owner', password='password123'
            )
        self.assignee = User.objects.create_user(
            username='assignee', password='password123'
            )
        self.other_user = User.objects.create_user(
            username='intruder', password='password123'
            )

        #
        self.project = Project.objects.create(
            owner=self.owner,
            title='Assignment Project',
            description='A project to test assignments',
            start_date=date.today(),
            end_date=date.today(),
            status='ongoing'
        )

        self.task = Task.objects.create(
            owner=self.owner,
            project=self.project,
            title='Assignment Task',
            description='A task to test assignments',
            status='pending'
        )

        self.assignment = VolunteerAssignment.objects.create(
            owner=self.owner,
            task=self.task,
            user=self.assignee,
        )

    def test_anonymous_can_view_assignments(self):
        response = self.client.get(f'/api/assignments/')
        assert response.status_code == status.HTTP_200_OK

    
    def test_owner_can_create_assignment(self):
        self.client.force_authenticate(user=self.owner)

        payload = {
            'task': self.task.id,
            'user': self.assignee.id
        }
        response = self.client.post('/api/assignments/', payload)
        assert response.status_code == status.HTTP_201_CREATED


    def test_non_owner_cannot_delete_assignment(self):
        self.client.force_authenticate(user=self.other_user)

        response = self.client.delete(
            f'/api/assignments/{self.assignment.id}/'
            )

        assert response.status_code == status.HTTP_403_FORBIDDEN