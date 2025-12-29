import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from projects.models import Project
from datetime import date


@pytest.mark.django_db
class TestProjectsAPI:

    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.project = Project.objects.create(
            owner=self.user,
            title='Test Project',
            description='A project for testing',
            start_date=date.today(),
            end_date=date.today(),
            status='upcoming'
        )

        def test_anonymous_can_view_projects(self):
            response = self.client.get('/api/projects/')
            assert response.status_code == status.HTTP_200_OK

        def test_authenticated_user_can_create_project(self):
            self.client.force_authenticate(user=self.user)

            payload = {
                'title': 'New Project',
                'description': 'A new project',
                'start_date': str(date.today()),
                'end_date': str(date.today()),
                'status': 'upcoming'
            }
            response = self.client.post('/api/projects/', payload)
            assert response.status_code == status.HTTP_201_CREATED
            assert Project.objects.count() == 2

        def test_non_owner_cannot_update_project(self):
            other_user = User.objects.create_user(username='otheruser', password='password123')
            self.client.force_authenticate(user=other_user)

            response = self.client.put(f'/api/projects/{self.project.id}/', {
                'title': 'Updated Title'})
            assert response.status_code == status.HTTP_403_FORBIDDEN