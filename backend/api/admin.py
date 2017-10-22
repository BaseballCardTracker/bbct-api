from django.contrib import admin

from .models import BrandName, PlayerName, TeamName, Position

admin.site.register(BrandName)
admin.site.register(PlayerName)
admin.site.register(TeamName)
admin.site.register(Position)
