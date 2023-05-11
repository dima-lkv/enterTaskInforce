from datetime import datetime

from rest_framework import viewsets

import custom_permissions
from menu.serializers import MenuSerializer
from menu.models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed or edited.
    """
    queryset = Menu.objects.all().order_by('restaurant_id')
    serializer_class = MenuSerializer
    permission_classes = [custom_permissions.GetPostAllOtherAdmin]


class TodayMenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows today menus to be viewed or edited.
    """
    serializer_class = MenuSerializer
    permission_classes = [custom_permissions.GetOnly]

    def get_queryset(self):
        return Menu.objects.filter(week_day=datetime.now().weekday()).order_by('restaurant_id')
