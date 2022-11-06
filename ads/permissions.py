from rest_framework import permissions

from user.models import UserRoles


class IsOwnerSelection(permissions.BasePermission):
    message = "У вас нет прав на редактирование"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsOwnerAdOrStaff(permissions.BasePermission):
    message = "У вас нет прав на редактирование"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            return True
        return False
