from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from accounts.models import CustomUser


class Attack(models.Model):
    """
    defender_X | defender_Y | attack_type | attacker_x | attacker_y | entry_time | send_time | defender_name | attacker_name

    """
    defender_x = models.IntegerField(default=0)
    defender_y = models.IntegerField(default=0)
    attacker_x = models.IntegerField(default=0)
    attacker_y = models.IntegerField(default=0)
    distance = models.IntegerField(default=0)
    attack_type = models.CharField(max_length=99)
    entry_time = models.DateTimeField()
    send_time = models.DateTimeField()
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
