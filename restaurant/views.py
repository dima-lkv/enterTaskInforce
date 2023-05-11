from utils import custom_permissions
from .models import Restaurant
from rest_framework import viewsets

from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows restaurants to be viewed or edited.
    """
    queryset = Restaurant.objects.all().order_by('id')
    serializer_class = RestaurantSerializer
    permission_classes = [custom_permissions.GetPostAllOtherAdmin]
