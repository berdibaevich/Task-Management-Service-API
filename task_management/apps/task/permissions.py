from rest_framework.permissions import BasePermission


class IsOwnerOfTask(BasePermission):
    """
        For task's detail permission, if user is authenticated and 
        owner of task
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated
    

    def has_object_permission(self, request, view, obj):
        return request.user.pk == obj.user.pk