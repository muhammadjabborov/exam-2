from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import CharField, ImageField, IntegerField, TextField, ForeignKey, CASCADE, SET_NULL
from rest_framework.fields import DateField

from apps.common.models import BaseModel


class Team(BaseModel):
    name = CharField(max_length=255)
    logo = ImageField(upload_to='logos/')
    titles = IntegerField(default=0)

    def __str__(self):
        return self.name


class News(BaseModel):
    title = CharField(max_length=255)
    image = ImageField(upload_to='images/')
    description = TextField()
    mentions = ArrayField(CharField(max_length=25))

    def __str__(self):
        return self.title


class Season(BaseModel):
    perioud = CharField(max_length=25)

    def __str__(self):
        return self.perioud


class Archive(BaseModel):
    season = ForeignKey('task5.Season', CASCADE)
    team = ForeignKey('task5.Team', CASCADE)

    def __str__(self):
        return self.team.name


class Standings(BaseModel):
    state = IntegerField()
    team = ForeignKey('task5.Team', CASCADE)
    mp = IntegerField(default=0)
    w = IntegerField(default=0)
    d = IntegerField(default=0)
    l = IntegerField(default=0)
    g = IntegerField(default=0)
    pts = IntegerField(default=0)

    def __str__(self):
        return self.team.name


class Result(BaseModel):
    game = IntegerField()
    date = DateField()
    team1 = ForeignKey('task5.Team', CASCADE, related_name='team1')
    team2 = ForeignKey('task5.Team', CASCADE, related_name='team2')
    winner = ForeignKey('task5.Team', SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.game


class Summary(BaseModel):
    date = DateField()
    stteam = ForeignKey('task5.Team', CASCADE, related_name='stteam')
    ndteam = ForeignKey('task5.Team', CASCADE, related_name='ndteam')

    def __str__(self):
        return self.date
