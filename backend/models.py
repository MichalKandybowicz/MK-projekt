from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from accounts.models import CustomUser


class Attack(models.Model):
    defender_cords = models.CharField(max_length=7)
    attacker_cords = models.CharField(max_length=7)
    distance = models.DecimalField(max_digits=6, decimal_places=1)
    attack_type = models.CharField(max_length=20)
    entry_time = models.DateTimeField()
    defender_name = models.CharField(max_length=99)
    attacker_name = models.CharField(max_length=99)

    def get_absolute_url(self):
        return reverse('movie-detail-view', args=[str(self.id)])


class VillageDetailInformation(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    troops_type = models.CharField(max_length=3, null=True, blank=True)  # off/def/
    lose_off = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
