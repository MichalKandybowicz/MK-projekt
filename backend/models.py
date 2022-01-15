from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.authtoken.models import Token
import uuid


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    level = models.IntegerField(default=1)
    gold = models.IntegerField(default=50)
    time_next_ritual = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    rituals_count = models.IntegerField(default=0)
    travel_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class MonsterStatisticIncrease(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    rarity_lvl = models.IntegerField(default=1)
    luck = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    vitality = models.IntegerField(default=1)
    wisdom = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    item_type = models.CharField(max_length=50, blank=True, null=True)
    min_price = models.IntegerField(blank=True, null=True)
    max_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    gold_min = models.IntegerField(default=1)
    gold_max = models.IntegerField(default=1)
    reward_1 = models.ForeignKey(Item, related_name="region_reward_1", on_delete=models.SET_NULL, blank=True, null=True)
    item_1_rate = models.IntegerField(default=1)
    reward_2 = models.ForeignKey(Item, related_name="region_reward_2", on_delete=models.SET_NULL, blank=True, null=True)
    item_2_rate = models.IntegerField(default=1)
    reward_3 = models.ForeignKey(Item, related_name="region_reward_3", on_delete=models.SET_NULL, blank=True, null=True)
    item_3_rate = models.IntegerField(default=1)
    reward_4 = models.ForeignKey(Item, related_name="region_reward_4", on_delete=models.SET_NULL, blank=True, null=True)
    item_4_rate = models.IntegerField(default=1)
    reward_5 = models.ForeignKey(Item, related_name="region_reward_5", on_delete=models.SET_NULL, blank=True, null=True)
    item_5_rate = models.IntegerField(default=1)
    reward_6 = models.ForeignKey(Item, related_name="region_reward_6", on_delete=models.SET_NULL, blank=True, null=True)
    item_6_rate = models.IntegerField(default=1)
    reward_7 = models.ForeignKey(Item, related_name="region_reward_7", on_delete=models.SET_NULL, blank=True, null=True)
    item_7_rate = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Monster(models.Model):
    models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    name_from_user = models.CharField(max_length=50, null=True, blank=True
                                      )
    level = models.IntegerField(default=1)
    player = models.ForeignKey(CustomUser, related_name="user_monster", on_delete=models.SET_NULL, null=True, blank=True)
    photo_front = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    photo_side = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    travel_region = models.ForeignKey(Region, related_name="monster_region", on_delete=models.SET_NULL, blank=True, null=True)
    travel_finish_time = models.DateTimeField(blank=True, null=True)
    feed_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    luck_from_feed = models.IntegerField(default=1)
    strength_from_feed = models.IntegerField(default=1)
    dexterity_from_feed = models.IntegerField(default=1)
    vitality_from_feed = models.IntegerField(default=1)
    wisdom_from_feed = models.IntegerField(default=1)
    intelligence_from_feed = models.IntegerField(default=1)
    stats_increase = models.ForeignKey(MonsterStatisticIncrease, related_name="user_monster", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    player = models.ForeignKey(CustomUser, related_name="warehouse_owner", on_delete=models.SET_NULL, blank=True, null=True)
    item = models.ForeignKey(Item, related_name="warehouse_item", on_delete=models.SET_NULL, blank=True, null=True)


class Shop(models.Model):
    player = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    free_change = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    item_1 = models.ForeignKey(Item, related_name="shop_item_1", on_delete=models.SET_NULL, blank=True, null=True)
    item_1_count = models.IntegerField(default=1)
    item_2 = models.ForeignKey(Item, related_name="shop_item_2", on_delete=models.SET_NULL, blank=True, null=True)
    item_2_count = models.IntegerField(default=1)
    item_3 = models.ForeignKey(Item, related_name="shop_item_3", on_delete=models.SET_NULL, blank=True, null=True)
    item_3_count = models.IntegerField(default=1)
    item_4 = models.ForeignKey(Item, related_name="shop_item_4", on_delete=models.SET_NULL, blank=True, null=True)
    item_4_count = models.IntegerField(default=1)
    item_5 = models.ForeignKey(Item, related_name="shop_item_5", on_delete=models.SET_NULL, blank=True, null=True)
    item_5_count = models.IntegerField(default=1)


class Ritual(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    item_1 = models.ForeignKey(Item, related_name="ritual_item_1", on_delete=models.SET_NULL, blank=True, null=True)
    item_2 = models.ForeignKey(Item, related_name="ritual_item_2", on_delete=models.SET_NULL, blank=True, null=True)
    item_3 = models.ForeignKey(Item, related_name="ritual_item_3", on_delete=models.SET_NULL, blank=True, null=True)
    item_4 = models.ForeignKey(Item, related_name="ritual_item_4", on_delete=models.SET_NULL, blank=True, null=True)
    item_5 = models.ForeignKey(Item, related_name="ritual_item_5", on_delete=models.SET_NULL, blank=True, null=True)
    item_6 = models.ForeignKey(Item, related_name="ritual_item_6", on_delete=models.SET_NULL, blank=True, null=True)
    item_7 = models.ForeignKey(Item, related_name="ritual_item_7", on_delete=models.SET_NULL, blank=True, null=True)
    item_8 = models.ForeignKey(Item, related_name="ritual_item_8", on_delete=models.SET_NULL, blank=True, null=True)
    item_9 = models.ForeignKey(Item, related_name="ritual_item_9", on_delete=models.SET_NULL, blank=True, null=True)
    reward_item = models.ForeignKey(Item, related_name="ritual_reward_item", on_delete=models.SET_NULL, blank=True, null=True)
    reward_monster = models.ForeignKey(Monster, related_name="ritual_reward_monster", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class ConfigLvl(models.Model):
    level = models.IntegerField(default=1)
    eating = models.IntegerField(default=1)