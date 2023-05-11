from datetime import datetime

from rest_framework import viewsets

import custom_permissions
from menu.serializers import MenuSerializer
from menu.models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed or edited.
    """
    queryset = Menu.objects.all().filter(created_at=datetime.now().strftime("%m/%d/%Y")).order_by('restaurant_id')
    serializer_class = MenuSerializer
    permission_classes = [custom_permissions.GetPostAllOtherAdmin]
