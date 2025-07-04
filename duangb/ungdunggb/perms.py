from rest_framework import permissions

class OwnerAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view, obj):
        return self.has_permission(request, view) and request.user == obj.user