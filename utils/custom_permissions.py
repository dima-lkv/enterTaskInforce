from datetime import datetime

from rest_framework.permissions import BasePermission
from vote.models import Vote


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


class GetOnly(BasePermission):
    """
    Authorized user can GET and POST.
    """

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return bool(request.user and request.user.is_authenticated)


class VoteGetPostAuthenticatedOtherAdmin(BasePermission):
    """
    Authorized user can GET and POST.
    POST only if no POST request this day
    """

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return bool(request.user and request.user.is_authenticated)
        elif request.method in ['POST']:
            today_votes = Vote.objects.all().filter(created_at=datetime.now().strftime("%m/%d/%Y"))
            if today_votes.filter(user_id=request.user.id):
                return False
            return bool(request.user and request.user.is_authenticated)
        else:
            return bool(request.user and request.user.is_staff)
