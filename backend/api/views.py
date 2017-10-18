from django.http.response import HttpResponse


def brand_names(request):
    return HttpResponse('Brand Names')


def player_names(request):
    return HttpResponse('Player Names')


def team_names(request):
    return HttpResponse('Team Names')


def positions(request):
    return HttpResponse('Positions')
