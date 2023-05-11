from datetime import datetime

from django.db.models import Count, F
from rest_framework import viewsets

import custom_permissions
from menu.serializers import MenuSerializer
from menu.models import Menu
from vote.models import Vote


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menus to be viewed or edited.
    """
    queryset = Menu.objects.all().order_by('restaurant_id')
    serializer_class = MenuSerializer
    permission_classes = [custom_permissions.GetPostAllOtherAdmin]


class TodayMenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows today menu to be viewed.
    """
    serializer_class = MenuSerializer
    permission_classes = [custom_permissions.GetOnly]

    def get_queryset(self):
        return Menu.objects.filter(week_day=datetime.now().weekday()).order_by('restaurant_id')


class WinnerMenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows today winner menu to be viewed.
    """
    serializer_class = MenuSerializer
    permission_classes = [custom_permissions.GetOnly]

    def get_queryset(self):
        today_votes = Vote.objects.filter(created_at=datetime.now().strftime("%m/%d/%Y"))
        votes = today_votes.values('menu_id').annotate(count=Count('menu_id')).order_by('-count')
        top_vote = votes.first()
        return Menu.objects.filter(id=top_vote['menu_id'])
