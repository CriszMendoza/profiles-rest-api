from rest_framework import permissions

class UpdatedOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is tryning to edit their own profile"""
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
