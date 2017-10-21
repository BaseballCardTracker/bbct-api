from django.core import serializers
from django.http.response import JsonResponse

from api.models import BrandName, PlayerName, TeamName, Position


def get_objects(model_class):
    objects = model_class.objects.all()
    json = serializers.serialize('json', objects)
    return JsonResponse(json, safe=False)


def get_brand_names(request):
    return get_objects(BrandName)


def get_player_names(request):
    return get_objects(PlayerName)


def get_team_names(request):
    return get_objects(TeamName)


def get_positions(request):
    return get_objects(Position)
