from .models import Menu
from rest_framework import serializers


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu

        fields = ['url', 'id', 'week_day', 'choice', 'restaurant_id']
