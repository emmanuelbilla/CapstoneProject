#from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VolunteerAssignmentViewSet

router = DefaultRouter()
router.register(r'assignments', VolunteerAssignmentViewSet, basename='assignments')


urlpatterns = router.urls