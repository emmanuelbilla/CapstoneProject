from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsProjectOwnerOrReadOnly(BasePermission):
    """
   Only project owners can create, update, or delete volunteer assignments.
Authenticated users can view assignments.
    """


    def has_permission(self, request, view):
        # Write actions require authentication
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Read-only always allowed
        if request.method in SAFE_METHODS:
            return True
        # Only project owner can modify
        return obj.task.project.owner == request.user