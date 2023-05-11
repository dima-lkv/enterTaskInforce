from utils import custom_permissions
from .models import Vote
from rest_framework import viewsets

from .serializers import VoteSerializer


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows votes to be viewed or edited.
    """
    queryset = Vote.objects.all().order_by('-id')
    serializer_class = VoteSerializer
    permission_classes = [custom_permissions.VoteGetPostAuthenticatedOtherAdmin]
