from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from accounts.models import CustomUser


class Village(models.Model):
    cords = models.CharField(max_length=7)

    def __str__(self):
        return str(self.cords)

    def __repr__(self):
        return self.cords


class Attack(models.Model):
    defender_cords = models.CharField(max_length=7)
    attacker_cords = models.ForeignKey(
        Village,
        related_name='villages_attacks',
        on_delete=models.PROTECT,
        null=True,
        blank=True)
    distance = models.DecimalField(max_digits=6, decimal_places=1)
    attack_type = models.CharField(max_length=20)
    entry_time = models.DateTimeField()
    defender_name = models.CharField(max_length=99)
    attacker_name = models.CharField(max_length=99)

    def get_absolute_url(self):
        return reverse('attack', args=[str(self.id)])

    @property
    def attacker_cords_name(self):
        return self.attacker_cords.cords


class Report(models.Model):
    attacker_cords = models.ForeignKey(Village, related_name='villages_reports', on_delete=models.SET_NULL, null=True,
                                       blank=True)
    battle_time = models.DateTimeField(null=True, blank=True)
    send_troops_off = models.IntegerField(null=True, blank=True)
    loos_troops_off = models.IntegerField(null=True, blank=True)
    send_troops_def = models.IntegerField(null=True, blank=True)
    loos_troops_def = models.IntegerField(null=True, blank=True)
    send_catapult = models.IntegerField(null=True, blank=True)
    loos_catapult = models.IntegerField(null=True, blank=True)
    attack_hash = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('report', args=[str(self.id)])
