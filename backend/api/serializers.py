from rest_framework import serializers

from api import models


class BaseballCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseballCard
        fields = '__all__'
