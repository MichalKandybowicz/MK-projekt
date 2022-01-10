import random
import string

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):

    in_work = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.username)


class TypesInGame(models.IntegerChoices):
    ZIEMIA = 1
    OGIEŃ = 2
    WODA = 3
    WIATR = 4


class MonsterSkill(models.Model):

    name = models.CharField(max_length=10)
    skill_type = models.IntegerField(choices=TypesInGame.choices)
    min_attack = models.IntegerField()
    max_attack = models.IntegerField()
    hit_rate = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Monster(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    skin = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    level = models.IntegerField()
    exp = models.IntegerField()
    feeding = models.IntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    in_team = models.BooleanField(default=False)
    in_market = models.BooleanField(default=False)
    in_travel = models.BooleanField(default=False)
    type = models.IntegerField(choices=TypesInGame.choices)

    strength_b = models.IntegerField()
    strength_p = models.IntegerField()
    strength_t = models.IntegerField()
    intelligence_b = models.IntegerField()
    intelligence_p = models.IntegerField()
    intelligence_t = models.IntegerField()
    VitalityB = models.IntegerField()
    VitalityP = models.IntegerField()
    VitalityT = models.IntegerField()
    AgilityB = models.IntegerField()
    AgilityP = models.IntegerField()
    AgilityT = models.IntegerField()
    KnowledgeB = models.IntegerField()
    KnowledgeP = models.IntegerField()
    KnowledgeT = models.IntegerField()
    LuckB = models.IntegerField()
    LuckP = models.IntegerField()
    LuckT = models.IntegerField()

    affection = models.IntegerField()

    skill_0 = models.ForeignKey(MonsterSkill, related_name='skill_0', on_delete=models.CASCADE)
    skill_1 = models.ForeignKey(MonsterSkill, related_name='skill_1', on_delete=models.CASCADE)
    skill_2 = models.ForeignKey(MonsterSkill, related_name='skill_2', on_delete=models.CASCADE)
    skill_3 = models.ForeignKey(MonsterSkill, related_name='skill_3', on_delete=models.CASCADE)
    skill_4 = models.ForeignKey(MonsterSkill, related_name='skill_4', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)