from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^brand_names/', views.get_brand_names, name='brand-names'),
    url(r'^player_names/', views.get_player_names, name='player-names'),
    url(r'^team_names/', views.get_team_names, name='team-names'),
    url(r'^positions/', views.get_positions, name='positions'),
]
