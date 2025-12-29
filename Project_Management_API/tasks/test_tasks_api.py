import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date

from projects.models import Project
from tasks.models import Task

@pytest.mark.django_db
class TestTasksAPI:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.other_user = User.objects.create_user(username='otheruser', password='password123')
        self.project = Project.objects.create(
            owner=self.user,
            title='Project for Tasks',
            description='A project to test tasks',
            start_date=date.today(),
            end_date=date.today(),
            status='upcoming'
        )

        self.task = Task.objects.create(
            owner=self.user,
            project=self.project,
            title='Initial Task',
            description='This is the first task',
            status='pending',
        )

        def test_anonymous_can_view_tasks(self):
            response = self.client.get(f'/api/tasks/')
            assert response.status_code == status.HTTP_200_OK
        
        def test_authenticated_user_can_create_task(self):
            self.client.force_authenticate(user=self.user)

            payload = {
                'project': self.project.id,
                'title': 'New Task',
                'description': 'A new task description',
                'status': 'pending'
            }

            response = self.client.post('/api/tasks/', payload)
            assert response.status_code == status.HTTP_201_CREATED
            assert Task.objects.count() == 2

        def test_non_owner_cannot_update_task(self):
            self.client.force_authenticate(user=self.other_user)

            response = self.client.patch(
                f'/api/tasks/{self.task.id}/', 
                {'title': 'Unauthorized Edit'}
            )

            assert response.status_code == status.HTTP_403_FORBIDDEN