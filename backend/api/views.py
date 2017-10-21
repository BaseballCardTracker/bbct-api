from django.core import serializers
from django.http.response import HttpResponse, JsonResponse

from api.models import BrandName, PlayerName, TeamName


def get_brand_names(request):
    brand_names = BrandName.objects.all()
    json = serializers.serialize('json', brand_names)
    return JsonResponse(json, safe=False)


def get_player_names(request):
    player_names = PlayerName.objects.all()
    json = serializers.serialize('json', player_names)
    return JsonResponse(json, safe=False)


def get_team_names(request):
    team_names = TeamName.objects.all()
    json = serializers.serialize('json', team_names)
    return JsonResponse(json, safe=False)


def get_positions(request):
    return HttpResponse('Positions')
