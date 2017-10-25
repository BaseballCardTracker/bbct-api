from django.conf.urls import url

from api.models import BrandName, Position, TeamName, PlayerName
from api.views import ModelListView

urlpatterns = [
    url(r'^brand_names/', ModelListView.as_view(model_class=BrandName), name='brand-names'),
    url(r'^player_names/', ModelListView.as_view(model_class=PlayerName), name='player-names'),
    url(r'^team_names/', ModelListView.as_view(model_class=TeamName), name='team-names'),
    url(r'^positions/', ModelListView.as_view(model_class=Position), name='positions'),
]
