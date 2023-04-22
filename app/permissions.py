from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.ower:
            return True

        if hasattr(obj, "owner"):
            owner = obj.owner
        elif hasattr(obj, "author"):
            owner = obj.author
        else:
            raise Exception("?????")


class IsStuff(BasePermission):

    def has_permission(self, request, view):
        if request.user.roles in [User.ADMIN, User.MODERATOR]:
            return True
