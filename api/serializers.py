from rest_framework import serializers

from api import models


class BaseballCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseballCard
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = '__all__'
