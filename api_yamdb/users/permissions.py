from rest_framework import permissions


# class IsAdmin(permissions.BasePermission):
#     """Редактирование объекта доступно админу."""
#
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.is_admin
#
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Чтение доступно всем, редактирование только админу."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)


class IsModerator(permissions.BasePermission):
    """Редактирование объекта доступно модератору."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator


class IsSuperuser(permissions.BasePermission):
    """Редактирование объекта доступно суперпользователю."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser
