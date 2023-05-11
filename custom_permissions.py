from rest_framework.permissions import BasePermission


class GetPostAllOtherAdmin(BasePermission):
    """
    Unauthorized user can GET and POST.
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class GetPostAuthenticatedOtherAdmin(BasePermission):
    """
    Authorized user can GET and POST.
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return bool(request.user and request.user.is_authenticated)
        else:
            return bool(request.user and request.user.is_staff)
