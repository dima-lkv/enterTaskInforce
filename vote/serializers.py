from .models import Vote
from rest_framework import serializers


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote

        fields = ['url', 'user_id', 'menu_id']
