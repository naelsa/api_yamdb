from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorModeratorAdminSuperuser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or request.user.is_superuser
                or obj.author == request.user)
