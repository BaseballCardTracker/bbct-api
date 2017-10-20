from django.http.response import HttpResponse


def get_brand_names(request):
    return HttpResponse('Brand Names')


def get_player_names(request):
    return HttpResponse('Player Names')


def get_team_names(request):
    return HttpResponse('Team Names')


def get_positions(request):
    return HttpResponse('Positions')
