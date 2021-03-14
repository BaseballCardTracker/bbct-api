from rest_framework import viewsets

from api import models, serializers


class BaseballCardViewSet(viewsets.ModelViewSet):
    queryset = models.BaseballCard.objects.all()
    serializer_class = serializers.BaseballCardSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer
