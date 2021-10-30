from rest_framework import serializers

from backend.models import Attack, VillageDetailInformation


class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ['url', 'defender_cords', 'attacker_cords', 'distance',
                  'attack_type', 'entry_time', 'defender_name', 'attacker_name']


class VillageDetailInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageDetailInformation
        fields = ['url', 'x', 'y', 'troops_type', 'lose_off', 'created', 'modified']
