from rest_framework import serializers
from .models import Desert


class DesertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Desert
        fields = ['id', 'name', 'types']
