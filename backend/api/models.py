from django.db import models


class BrandName(models.Model):
    brand_name = models.CharField(max_length=25)


class PlayerName(models.Model):
    player_name = models.CharField(max_length=25)


class TeamName(models.Model):
    team_name = models.CharField(max_length=25)


class Position(models.Model):
    position = models.CharField(max_length=25)
