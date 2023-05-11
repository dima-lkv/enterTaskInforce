from .models import Restaurant
from rest_framework import serializers


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['url', 'id', 'name', 'menu']
