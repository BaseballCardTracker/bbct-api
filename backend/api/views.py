from rest_framework import permissions, viewsets

from api import models, serializers


class BaseballCardViewSet(viewsets.ModelViewSet):
    queryset = models.BaseballCard.objects.all()
    serializer_class = serializers.BaseballCardSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CollectionSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Collection.objects.all()
        return models.Collection.objects.filter(user=self.request.user)
